from django import forms 

from .models import Crimes , CategoryChoice , StatusChoices

class CrimeReportForm(forms.ModelForm):
    


    class Meta:

        model = Crimes

        # fields = '__all__'

        exclude = ['uuid','active_status','police_officer']

        widgets ={
                 
                 'reporting_user' : forms.TextInput(attrs={
                     
                                                            'class': 'form-control',

                                                            'placeholder' : 'Enter a name',
                                                            
                                                            'required' : 'required'


                                                        }),

                 'title' : forms.TextInput (attrs={

                                                 'class' : 'form-control',

                                                 'placeholder' : 'Enter the title',

                                                 'required' : 'required'
                                               }),

                  'reporting_date' : forms.DateInput(attrs={
                                                
                                                        'class' : 'form-control',

                                                        'required' : 'required'
                                                          
                                                          }),

        }

        category = forms.ChoiceField (choices=CategoryChoice.choices,widget=forms.Select(attrs={
                                                                                     
                                                                                     'class':'form-select',

                                                                                     'required' : 'required'
                                                                                     }))   ,

        
        level = forms.ChoiceField(choices=StatusChoices.choices,widget=forms.Select(attrs={ 'class':'form-select',
                                                                                          
                                                                                     'required' : 'required'
                                                                                     }))
        
        def __init__(self,*args,**kwargs):

            super(CrimeReportForm,self).__init__(*args,**kwargs)   
        
        
    

                               