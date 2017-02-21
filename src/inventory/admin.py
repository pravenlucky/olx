from django.contrib import admin

from .models import Item, Comment


class ItemAdmin(admin.ModelAdmin):
    list_display = ['title','pub_date']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','pub_date']

admin.site.register(Item, ItemAdmin)
admin.site.register(Comment, CommentAdmin)