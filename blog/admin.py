from django.contrib import admin
from .models import Comment, Asset
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Asset)
class AssetAdmin(SummernoteModelAdmin):
    # add the asset models to the admin panel
    # apply summernote to the content text field
    # prepopulate slug with title, add filter, listdisplay, search functionality

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'asset', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
