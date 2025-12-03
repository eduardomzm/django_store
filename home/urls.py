from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'), #'home:index'
    path('profile/', views.profile, name="profile"),
    path('register/', views.register, name="register"),
]

