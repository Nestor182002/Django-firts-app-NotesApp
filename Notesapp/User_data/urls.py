from django.urls import path

# login and register
from .views import LoginView, RegisterView

#IMPORTAR LOGOUT
from django.contrib.auth.views import LogoutView   

urlpatterns = [
    # registro y manejo de usuarios
    path("login/",LoginView.as_view(),name="login"),
    path("logout/",LogoutView.as_view(next_page="login"),name="logout"),
    path("register/",RegisterView.as_view(),name="register"),


    
]