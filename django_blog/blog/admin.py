from django.contrib import admin
from .models import Post

# Register your models here.
# This will make Post model/db available on admin gui 
admin.site.register(Post)

