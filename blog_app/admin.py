from django.contrib import admin

# Register your models here.
from .models import Blog, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Blog, PostAdmin)
admin.site.register(Comment)