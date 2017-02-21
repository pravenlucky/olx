from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
    post_checkout,
    soon,
    home,
    sign_in,
    sign_out,
    register,
    edit,

)

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name='delete'),
    url(r'^(?P<slug>[\w-]+)/checkout/$', post_checkout, name='checkout'),
    url(r'^(?P<slug>[\w-]+)/register_home$', home, name='home'),
    url(r'^(?P<slug>[\w-]+)/register/$', register, name='register'),
    url(r'^(?P<slug>[\w-]+)/sign_in/$', sign_in, name='sign_in'),
    url(r'^(?P<slug>[\w-]+)/sign_out/$', sign_out, name='sign_out'),

    #url(r'^(?P<slug>[\w-]+)/edit$/', edit, name='edit'),

    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^admin/', include(admin.site.urls)),

]
