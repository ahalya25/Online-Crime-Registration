from django.urls import path

from . import views

urlpatterns =[
    path('crimes-list/',views.CrimeListView.as_view(),name='crimes-list'),

    path('home/',views.HomeView.as_view(),name='home'),

    path('about/',views.CrimesAboutView.as_view(),name='about'),

    path('login/',views.CrimesLoginView.as_view(),name='login'),

    path('contact/',views.CrimesContactView.as_view(),name='contact'),  

    path('report-crime/',views.CrimeReportCreation.as_view(),name='report-crime'),

    path('crime-detail-view/<str:uuid>/',views.CrimeDetailsView.as_view(),name='crime-detail-view'),

    path('crime-detail-delete/<str:uuid>/',views.CrimeDetailsDeleteView.as_view(),name='crime-detail-delete'),

    path('crime-detail-update/<str:uuid>/',views.CrimeDetailsUpdateView.as_view(),name='crime-detail-update')




]