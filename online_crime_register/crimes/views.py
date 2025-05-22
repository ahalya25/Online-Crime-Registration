from django.shortcuts import render ,redirect

# Create your views here.

from django.views import View

from . models import Crimes,CategoryChoice,StatusChoices

# Create your views here.

# from police_officers.models import PoliceOfficers

from .forms import CrimeReportForm

from django.db.models import Q

from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from authentication.permissions import permission_roles

@method_decorator(permission_roles(roles=['Officers']),name='dispatch')
class CrimeListView(View):

    def get(self,request,*args,**kwargs):

        query = request.GET.get('query')

        # fetching all courses from courses model

        crimes = Crimes.objects.all()

        if query :

            crimes = Crimes.objects.filter(Q(reporting_user__icontains=query)|
                                             Q(police_officer__name__icontains=query)|
                                             Q(category__icontains=query)|
                                             Q(reporting_date__icontains=query)|
                                             Q(status__icontains=query))

       

        data = {'crimes':crimes, 'page':'crimes-list','query' : query}

        return render(request,'crimes/crimes-list.html',context=data)
    

    
class HomeView(View):

    def get(self,request,*args,**kwargs):

        data = {'page':'home-page'}

        return render(request,'crimes/home.html',context=data)  
    

    
class CrimesAboutView(View):

    def get(self,request,*args,**kwargs):

        data = {'page':'about-page'}

        return render(request,'crimes/about.html',context=data) 
    


class CrimesLoginView(View):

    def get(self,request,*args,**kwargs):

        data = {'page':'login-page'}

        return render(request,'crimes/login.html',context=data)      
    
    

class CrimesContactView(View):

    def get(self,request,*args,**kwargs):

        data = {'page':'contact-page'}

        return render(request,'crimes/contact.html',context=data)     
    

@method_decorator(permission_roles(roles=['Officers']),name='dispatch')
class CrimeReportCreation(View):

    def get(self,request,*args,**kwargs):

        form = CrimeReportForm()

        data = {'form': form ,'page': 'report-page'}    

        return render(request,'crimes/report-crime.html',context=data)
    
    def post(self,request,*args,**kwargs):


        # crime.save()
        
        form = CrimeReportForm(request.POST,request.FILES)

        print(form.errors)
        
        # police_officer = PoliceOfficers.objects.get(id=1)

        if form.is_valid():

            form.save()

            return redirect('crimes-list')
        
        data = {'form' : form }

        return render(request,'crimes/report-crime.html',context=data)
    

# @method_decorator(permission_roles(roles=['Officers']),name='dispatch')    
class CrimeDetailsView(View):

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        crime = Crimes.objects.get(uuid=uuid)

        # police_officer = PoliceOfficers.objects.get(id)

        # crime = Crimes.objects.filter(police_officer = police_officer)

        data ={'crime' : crime }

        return render(request,'crimes/crime-detail-view.html',context=data)
    
    
# @method_decorator(permission_roles(roles=['Officers']),name='dispatch')
class CrimeDetailsDeleteView(View):

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        crime = Crimes.objects.get(uuid=uuid)

        crime.delete()

        return redirect('crimes-list')     
    

@method_decorator(permission_roles(roles=['Officers']),name='dispatch')
class CrimeDetailsUpdateView(View):

    def get(self,request,*args,**kwargs) :

        uuid = kwargs.get('uuid')

        crime = Crimes.objects.get(uuid=uuid)

        form = CrimeReportForm(instance=crime)

        data = {'form' : form }  

        return render(request,'crimes/crime-detail-update.html',context=data)   
    
    def post(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        crime = Crimes.objects.get(uuid=uuid)

        form = CrimeReportForm(request.POST , request.FILES , instance = crime)

        if form.is_valid():

            form.save()

            return redirect('crimes-list')
        
        data = { 'form' : form }

        return render(request,'crimes/crime-detail-update.html',context = data)





            
