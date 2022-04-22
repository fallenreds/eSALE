from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(MyUser)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Status)