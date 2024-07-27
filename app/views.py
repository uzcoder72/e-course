from django.shortcuts import render, get_object_or_404
from .models import Category, Course, Comment

def index(request):
    categories = Category.objects.all()
    courses = Course.objects.all()
    return render(request, 'index.html', {'categories': categories, 'courses': courses})

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    comments = course.comments.all()
    return render(request, 'single.html', {'course': course, 'comments': comments})

def teacher(request):
    return render(request, 'teacher.html')

