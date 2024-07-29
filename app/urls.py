from django.contrib import admin
from django.urls import path, include
from config import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('teacher/', views.teacher, name='teacher'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
