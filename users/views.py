    
from django.shortcuts import render , redirect

# Create your views here.
from django.views import View

from .forms import ProfileForm , UsersForm

from django.contrib.auth.hashers import make_password

from django.db import transaction

from online_crime_register.utility import send_email

import threading

class UsersRegisterView(View):

    def get(self,request,*args,**kwargs):

        profile_form = ProfileForm()

        user_form = UsersForm()

        data = {'profile_form' : profile_form,'user_form':user_form}

        return render(request,'users/user-register.html',context=data)

        
    
    def post(self, request, *args , **kwargs):

        profile_form = ProfileForm(request.POST)

        print(profile_form.errors)

        user_form = UsersForm(request.POST, request.FILES)

        print(user_form.errors)



        if profile_form.is_valid():

            with transaction.atomic():

                profile = profile_form.save(commit=False)

                email = profile_form.cleaned_data.get('email')

                password = profile_form.cleaned_data.get('password')

                profile.username = email

                profile.role = 'User'

                profile.password = make_password(password)

                profile.save()

                if user_form.is_valid():

                    user = user_form.save(commit=False)

                    user.profile = profile

                    user.name = f'{profile.first_name} {profile.last_name}'

                    user.save()

                    subject = 'Successfully Registerd'

                    recipient = user.profile.email

                    template = 'email/success-registration.html'

                    context = {'name':user.name, 'username' : user.profile.email,'password':password }

                    # send_email(subject,recipient,template,context)
                    thread = threading.Thread(target=send_email,args=(subject,recipient,template,context))

                    thread.start() 

                    return redirect('login')
            
        data = {'profile_form' : profile_form, 'user_form': user_form}

        return render(request,'users/user-register.html',context=data)    