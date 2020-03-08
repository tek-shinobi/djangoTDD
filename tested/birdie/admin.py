from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('excerpt',)

    def excerpt(self, obj=None):
        return obj.body[:5]

