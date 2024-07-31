from django.urls import path
from .views import (
    BlogsPage,
    SinglePage,
    AuthenticationView,
    IndexPage,
    BaseIndexPage,
    CoursesPage,
    CDetailPage,
    CGDetailPage,
    ContactPage,
    AboutPage,
    TeachersPage,
    TeachersDetail,
    LogoutView
)

urlpatterns = [
    path('index/', IndexPage.as_view(), name='index'),
    path('base/', BaseIndexPage.as_view(), name='base'),

    path('blogs/', BlogsPage.as_view(), name='blog'),
    path('blog/single/<slug>/', SinglePage.as_view(), name='blog_detail'),

    path('auth/', AuthenticationView.as_view(), name='auth'),

    path('courses/', CoursesPage.as_view(), name='course'),
    path('course/<slug>/', CDetailPage.as_view(), name='course_detail'),
    path('category/<slug>/', CGDetailPage.as_view(), name='category_detail'),


    path('contact/', ContactPage.as_view(), name='contact'),
    path('about/', AboutPage.as_view(), name='about'),

    path('teachers/', TeachersPage.as_view(), name='teacher'),
    path('teacher/<slug>/', TeachersDetail.as_view(), name='teacher_detail'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
