from app.models import Blog
from app.models import Course, Category, Comment
from app.models import Teacher
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Category, Blog
class BlogsPage(View):
    def get(self, request):
        blogs = Blog.objects.all()
        categories = Category.objects.all()
        num_of_categories = len(categories)

        context = {'blogs': blogs,
                   'categories': categories,
                   'num_of_categories': num_of_categories,
                   'active_page': 'blog'}

        return render(request, 'blog.html', context)


class SinglePage(View):
    def get(self, request, slug):
        category = None
        print(slug)
        if slug == '/blog/single/None':
            category = Category.objects.get(slug=slug)
        categories = Category.objects.all()
        num_of_categories = len(categories)

        context = {'category': category,
                   'categories': categories,
                   'num_of_categories': num_of_categories,
                   'active_page': 'blog'}

        return render(request, 'blog_detail.html', context)




class AuthenticationView(View):
    def get(self, request):
        return render(request, 'auth.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to home page or any other page
        else:
            return render(request, 'auth.html', {'error': 'Invalid username or password'})


class IndexPage(View):
    def get(self, request):
        categories = Category.objects.all()
        teachers = Teacher.objects.all()
        courses = Course.objects.all()
        blogs = Blog.objects.all()

        context = {'categories': categories,
                   'teachers': teachers,
                   'courses': courses,
                   'blogs': blogs,
                   'active_page': 'home'}

        return render(request, 'index.html', context)


class BaseIndexPage(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {'categories': categories, }

        return render(request, 'base.html', context)


class CoursesPage(View):
    def get(self, request):
        categories = Category.objects.all()
        course = Course.objects.all()

        context = {'categories': categories,
                   'courses': course,
                   'active_page': 'courses'}

        return render(request, 'course.html', context)


# views.py
class CDetailPage(View):
    def get(self, request, slug):
        course = Course.objects.get(slug=slug)
        comments = Comment.objects.filter(course_id__slug=slug)
        categories = Category.objects.all()
        blogs = Blog.objects.all()

        context = {'course': course,
                   'comments': comments,
                   'categories': categories,
                   'blogs': blogs, }

        return render(request, 'course_detail.html', context)


# views.py


class CGDetailPage(View):
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        categories = Category.objects.all()
        blogs = Blog.objects.all()

        context = {'category': category,
                   'categories': categories,
                   'blogs': blogs, }

        return render(request, 'category_detail.html', context)




class ContactPage(View):
    def get(self, request):
        categories = Category.objects.all()

        context = {'categories': categories,
                   'active_page': 'contact'}

        return render(request, 'contact.html', context)


class AboutPage(View):
    def get(self, request):
        comments = Comment.objects.all()
        categories = Category.objects.all()

        context = {'comments': comments,
                   'categories': categories,
                   'active_page': 'about'}

        return render(request, 'about.html', context)




class TeachersPage(View):
    def get(self, request):
        categories = Category.objects.all()
        teachers = Teacher.objects.all()

        context = {
            'active_page': 'teachers',
            'categories': categories,
            'teachers': teachers,
        }

        return render(request, 'teacher.html', context)




class TeachersDetail(View):
    def get(self, request, slug):
        teacher = get_object_or_404(Teacher, slug=slug)
        categories = Category.objects.all()

        context = {
            'teacher': teacher,
            'categories': categories,
        }

        return render(request, 'teacher_detail.html', context)

from django.contrib.auth import logout
from django.shortcuts import redirect

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('auth')

