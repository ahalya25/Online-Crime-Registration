from django.urls import path

from . import views

urlpatterns = [

    path('officer-register/',views.OfficerRegisterView.as_view(),name='officer-register')
]