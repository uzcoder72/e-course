from django.contrib import admin
from .models import Category, Course, Comment

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Comment)