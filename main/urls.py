from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name = 'home'),
    path('about', views.about, name = 'about'),
    path('contacts', views.contact, name = 'contacts'),

    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('register/', views.register, name='register'),
]