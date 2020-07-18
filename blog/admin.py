from django.contrib import admin
from .models import Blogger, Blog, Comment

admin.site.register(Blogger)
admin.site.register(Blog)
admin.site.register(Comment)