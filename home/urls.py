from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
     path('',views.index),
     path('',views.login),
     path('contact/', views.contact),
     path('chon_hang/', views.chon_hang),
     # path('chon_hang/', views.chon_hang),
      path('register/', views.register, name="register"),
     path('login/',auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
     path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
]

