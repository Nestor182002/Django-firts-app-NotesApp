from django.contrib import admin

# Register your models here.
from posts.models import PostsModels, ComentPosts




admin.site.register(PostsModels)
admin.site.register(ComentPosts)

