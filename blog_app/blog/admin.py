from django.contrib import admin
from .models import Comment, Post

admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'post', 'created_at')
    list_filter = ('created_at', 'active')
    search_fields = ('name', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
