from django.urls import path

from . import views

urlpatterns = [

    path('user-register/',views.UsersRegisterView.as_view(),name='user-register')
]