from django.contrib import admin
from .models import CustomQuestion, Profile
# Register your models here.
admin.site.register(CustomQuestion)
admin.site.register(Profile)