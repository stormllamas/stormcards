from django.contrib import admin
from .models import Posts

# Register your models here.

# This allows posting of posts in the site
admin.site.register(Posts)