from django.contrib import admin

# Register your models here.
from .models import Post, Stripe_User

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_display_links = ["updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]

    search_fields = ["title", "content"]
    class Meta:
        model = Post

class Stripe_UserModel(admin.ModelAdmin):
    list_display = ["name", "email"]
    class Meta:
        model = Stripe_User

admin.site.register(Post, PostModelAdmin)
admin.site.register(Stripe_User, Stripe_UserModel)