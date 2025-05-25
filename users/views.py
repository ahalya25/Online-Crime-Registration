from django.shortcuts import render

# Create your views here.
from django.views import View

class UsersRegisterView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'users/user-register.html')