from django.urls import path

from user import views

urlpatterns = [
    path('register/', views.show_reg),
    path('login/', views.show_login),
    path('logout/', views.do_logout)
    ]