from webbrowser import register

from django.contrib import admin

from django.contrib.auth.models import Permission

from Board.models import Post, Message

# Register your models here.

admin.site.register(Post)

admin.site.register(Message)