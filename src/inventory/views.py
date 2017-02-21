from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from django.template.context_processors import csrf

from .models import Item, Comment
from .forms import ItemForm, CommentForm
from django.utils import timezone


def index(request):
    items = Item.objects.exclude(likes=100)
    return render(request, 'inventory/index.html', {
        'items': items,
        })


def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404('this item doesn\'t exist')
    return render(request, 'inventory/item_detail.html', {
        'item': item,
        })
    return


def hello(request):
    name = "praveen"
    html = "<html> <body> hi %s this is a simple html page</body> </html>" % name
    return HttpResponse(html)


def hello_template(request):
    name = "praveen"
    t = get_template('hello.html')
    html = t.render(Context({'name': name}))
    return HttpResponse(html)


def hello_simple(request):
    return render_to_response('hello.html', {'name': "praveen"})


class HelloTemplate(TemplateView):
    template_name = 'hello.html'

    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = 'praveen'
        return context


def articles(request):
    language = 'en-gb'
    session_language = 'en-gb'

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    if 'lang' in request.session:
        session_language = request.session['lang']

    return render_to_response('articles.html', {'articles': Item.objects.all(), 'language': language,
                                                'session_language': session_language, 'user': request.user})


def article(request, inventory_id=1):
    args = {}
    args['user'] = request.user
    args['article'] = Item.objects.get(id=inventory_id)
    return render_to_response('article.html', args)


def language(request, lang='en-gb'):
    response = HttpResponse("setting language to : %s" % lang)
    response.set_cookie('lang', lang)

    request.session['lang'] = lang
    return response


def create(request):
    if request.POST:
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inventory/all')
    else:
        form = ItemForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form
    # if request.user.is_authenticated():
    args['user'] = request.user
    return render_to_response('create_item.html', args)


def like(request, inventory_id):
    if inventory_id:
        a = Item.objects.get(id=inventory_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()
    return HttpResponseRedirect('/inventory/get/%s' % inventory_id)


def add_comment(request, inventory_id):
    a = Item.objects.get(id=inventory_id)
    if request.method == "POST":
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.item = a
            c.save()
            return HttpResponseRedirect('/inventory/get/%s' % inventory_id)

    else:
        f = CommentForm()

    args = {}
    args.update(csrf(request))
    args['article'] = a
    args['form'] = f
    args['user'] = request.user
    return render_to_response('add_comment.html', args)