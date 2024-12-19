from django.contrib import admin
from .models import UserProfile

from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(FollowersCount)
admin.site.register(Comment)
admin.site.register(LikePost)
# admin.py

admin.site.register(UserProfile)



