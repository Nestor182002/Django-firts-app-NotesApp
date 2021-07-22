from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect

#importar login y logout 
from django.contrib.auth.views import LoginView

# para el registro
from django.views.generic.edit import FormView
from User_data.form import UserRegisterForm


# Create your views here.

#login
class UserLogin(LoginView):
    template_name = "registration/login.html"
    fiels = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return redirect('posts')

class RegisterView(FormView):
    template_name="registration/register.html"
    form_class = UserRegisterForm
    redirect_authenticated_user=True
    success_url=reverse_lazy("login")

    def form_valid(self,form):
        user=form.save()
        if user is not None:
            return super(RegisterView,self).form_valid(form)



    

