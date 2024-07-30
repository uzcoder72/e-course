from django.shortcuts import render, get_object_or_404
from .models import Category, Course, Comment, Blog, Teacher

def index(request):
    categories = Category.objects.all()
    courses = Course.objects.all()
    return render(request, 'index.html', {'categories': categories, 'courses': courses})

def about(request):
    return render(request, 'about.html')

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = blog.comments.all()
    return render(request, 'blog_detail.html', {'blog': blog, 'comments': comments})

def contact(request):
    return render(request, 'contact.html')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    comments = course.comments.all()
    return render(request, 'single.html', {'course': course, 'comments': comments})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher.html', {'teachers': teachers})

def teacher_detail(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    return render(request, 'teacher_detail.html', {'teacher': teacher})
