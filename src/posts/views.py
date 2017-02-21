try:
    from urllib import quote_plus  # python 2
except :
    pass
try:
    from urllib.parse import quote_plus  # python 3
except :
    pass

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils import timezone
from django.template.context_processors import csrf
from django.db import IntegrityError
from django.template import RequestContext

from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import *
from .models import *
import stripe

import datetime

#import src.trydjango19.settings as settings



stripe.api_key = settings.STRIPE_SECRET


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        html = "<html> <body> <h2>sorry your are not an admin user</h2></body> </html>"
        return HttpResponse(html)

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        }
    return render(request, "post_form.html", context)


def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    # if instance.publish > timezone.now().date() or instance.draft:
    # if not request.user.is_staff or not request.user.is_superuser:
    #         raise Http404
    share_string = quote_plus(instance.content)
    context = {
        "title": instance.title,
        "instance": instance,
        "share_string": share_string,
        "user": request.user,
        }
    return render(request, "post_detail.html", context)


def post_list(request):
    today = timezone.now().date()
    # queryset_list = Post.objects.active() #.order_by("-timestamp")
    #if request.user.is_staff or request.user.is_superuser:
    queryset_list = Post.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 8)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    #except EmptyPage:
        ##If page is out of range (e.g. 9999), deliver last page of results.
        #queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var,
        "today": today,
        "user": request.user,
        }
    return render(request, "post_list.html", context)


def post_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    url = instance.get_absolute_url()
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
        "url": url,
        }
    return render(request, "post_form.html", context)


def post_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("posts:list")

###############################################################################


@login_required
def post_checkout(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    price = instance.price*100

    publishKey = "pk_test_ZQv3SAiAFPs4NDgNRjDWABJG"
    if request.method == 'POST':
        token = request.POST['stripeToken']
        try:
            charge = stripe.Charge.create(
                amount=price,
                currency="usd",
                source=token,
                description="Example charge",
                )
        except stripe.error.CardError as e:
            pass

    context = {}
    context.update(csrf(request))
    context['publishkey'] = publishKey
    context['price'] = price
    #price= instance.price
    return render(request, 'checkout.html', context)



















def soon():
    soon = datetime.date.today() + datetime.timedelta(days=30)
    return {'month': soon.month, 'year': soon.year}

def home(request, slug=None):

    uid = request.session.get('user')
    if uid is None:
        return render_to_response('home.html')
    else:
        return render_to_response('user.html', {'user': Stripe_User.objects.get(pk=uid)})

def sign_in(request, slug=None):
    user = None
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            results = Stripe_User.objects.filter(email=form.cleaned_data['email'])
            if len(results) == 1:
                if results[0].check_password(form.cleaned_data['password']):
                    request.session['user'] = results[0].pk
                    return HttpResponseRedirect('/')
                else:
                    form.addError('Incorrect email address or password')
            else:
                form.addError('Incorrect email address or password')
    else:
        form = SignInForm()

    print(form.non_field_errors())

    return render(request, 'sign_in.html',
        {
            'form': form,
            'user': user
        },
    )

def sign_out(request, slug=None):
    del request.session['user']
    return HttpResponseRedirect('/')

def register(request, slug=None):
    user = None
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():

            customer = stripe.Customer.create(
                description=form.cleaned_data['email'],
                card=form.cleaned_data['stripe_token'],
                # plan = 'basic'
            )

            user = Stripe_User(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                last_4_digits=form.cleaned_data['last_4_digits'],
                stripe_id=customer.id
            )
            user.set_password(form.cleaned_data['password1'])

            try:
                user.save()
            except IntegrityError:
                form.addError(user.email + ' is already a member')
            else:
                request.session['user'] = user.pk
                return HttpResponseRedirect('/')

    else:
        form = UserForm()

    return render(request,'stripe_register.html',
            {
            'form': form,
            'months': range(1, 13),
            'publishable': settings.STRIPE_PUBLISHABLE,
            'soon': soon(),
            'user': user,
            'years': range(2011, 2036),
            }
    )

def edit(request, slug=None):
    uid = request.session.get('user')
    if uid is None:
        return HttpResponseRedirect('/')
    user = Stripe_User.objects.get(pk=uid)
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            customer = stripe.Customer.retrieve(user.stripe_id)
            customer.card = form.cleaned_data['stripe_token']
            customer.save()

            user.last_4_digits = form.cleaned_data['last_4_digits']
            user.stripe_id = customer.id
            user.save()

            return HttpResponseRedirect('/')

    else:
        form = CardForm()

    return render(request,'edit.html',
        {
            'form': form,
            'publishable': settings.STRIPE_PUBLISHABLE,
            'soon': soon(),
            'months': range(1, 13),
            'years': range(2011, 2036)
        }
    )

