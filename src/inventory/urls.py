from django.conf.urls import url, include
from django.contrib.auth.views import (password_reset, password_reset_done,
                                       password_reset_confirm, password_reset_complete, password_change,
                                       password_change_done,)
from .import views
from .import view

urlpatterns = [
    url(r'^all/$', views.articles),
    url(r'^get/(?P<inventory_id>\d+)/$', views.article),
    url(r'^language/(?P<lang>[a-z\-]+)/$',views.language),
    url(r'^create/$', views.create),
    url(r'^add_comment/(?P<inventory_id>\d+)/$', views.add_comment),
    url(r'^like/(?P<inventory_id>\d+)/$', views.like),


    url(r'^$', views.articles, name='index'),
    url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
    url(r'^hello/$', views.hello),
    url(r'^hello_simple/$', views.hello_simple),
    url(r'^hello_template/$', views.hello_template),
    url(r'^hello_class/$', views.HelloTemplate.as_view()),
    url(r'^auth/$', view.auth_view),
    url(r'^login/$', view.login_view),
    url(r'^logged_in/$', view.logged_in_view),
    url(r'^logout/$', view.logout_view),
    url(r'^invalid/$', view.invalid_view),
    url(r'^register/$', view.register_view, name='register'),
    url(r'^registered/$', view.registered_view),
    url(r'^verification/$', view.verification_view),
    url(r'^edit_profile/$', view.edit_profile),
    url(r'^reset-password/$', password_reset, name='reset-password'),
    url(r'^reset-password/done/$', password_reset_done, name= 'password_reset_done'),
    url(r'^reset-password/complete/$', password_reset_complete, name= 'password_reset_complete'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm, name= 'password_reset_confirm'),
    url(r'^password/change/$', password_change, name='password_change'),
    url(r'^password/change/done/$', password_change_done, name='password_change_done'),

    ]