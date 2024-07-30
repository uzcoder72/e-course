from django.contrib import admin
from .models import Category, Course, Comment, Blog, BlogImage, Teacher, Author

class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1

class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogImageInline]
    list_display = ('title', 'date_added')
    search_fields = ('title', 'content')
    list_filter = ('date_added', 'auther_id')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'level')
    search_fields = ('full_name', 'description')
    list_filter = ('level',)

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Comment)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Author)
