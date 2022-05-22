from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    # add the post models to the admin panel
    # apply summernote to the content text field

    summernote_fields = ('content')

