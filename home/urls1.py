from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.aboutus, name='about'),
    path('courses/',views.courses, name='courses'),
    path('contact/', views.contact, name='contact'),
    path('courses/n3/',views.n3,name="n3"),
    path('courses/n4/',views.n4,name="n4"),
    path('courses/n5/', views.n5, name="n5"),

]