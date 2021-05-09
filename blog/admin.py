from django.contrib import admin
from .models import UserProfile,Post,Comments
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Comments)