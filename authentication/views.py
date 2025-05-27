from django.shortcuts import render,redirect

from django.views import View

from . forms import LoginForm

from . models import Profile

from django.contrib.auth import authenticate,login,logout

# Create your views here.

class LoginView(View):

    def get(self,request,*args,**kwargs):

        form = LoginForm()

        data = {'page' : 'login-page', 'form' : form }

        return render(request,'authentication/login.html',context=data)
    

    def post(self,request,*args,**kwargs):

        form = LoginForm(request.POST)

        error = None

        if form.is_valid():

            username = form.cleaned_data.get('username')

            password = form.cleaned_data.get('password')

            user = authenticate(username=username,password=password)

            if user :

                login(request,user)

                return redirect('crimes-list')
            
            error = 'invalid credentials'

        data = {'form' : form , 'error' : error,'page':'login'}    

        return render (request,'authentication/login.html',context=data)

class LogoutView(View):

    def get(self,request,*args,**kwargs) :

        logout (request)

        return redirect('crimes-list')   



class RegisterChoicesView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'authentication/register-choices.html')  
    
    def post(self,request,*args,**kwargs):

        role = request.POST.get('role')

        if role == 'user':

            return redirect('user-register')
        
        elif role == 'police-officer':

            return redirect('home')