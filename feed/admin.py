from django.contrib import admin
from .models import Post, Comments, Like

admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Like)
