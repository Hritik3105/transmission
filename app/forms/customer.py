from django.forms import ModelForm
from django import forms
from app.models import *


class CustomerCreateForm(ModelForm):
    passport_id = forms.CharField(required = True,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Enter passport_id'
        }  
    ))

    passport_upload = forms.FileField(required = True)

    passport_expiry = forms.DateField(required = True,widget=forms.DateInput(
        attrs={
        'class':'form-control',
        'type': 'date',
        'placeholder':'Enter Passport Expiry date'
        }
    ))
    
    name = forms.CharField(required = True,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Enter name'
        }
    ))
    country = forms.CharField(required = True,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter your country'
        }
    ))
    
    phone = forms.CharField(required = True,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Enter your Phone Number'
        }
    ))

    address = forms.CharField(required = True,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Enter your address'
        }
    ))

    rfc = forms.CharField(required = False,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Enter rfc'
        }
    ))

    curp = forms.CharField(required = False,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Enter your curp'
        }
    ))

    state = forms.CharField(required = True,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Enter State'
        }
    ))

    city= forms.CharField(required = True,widget=forms.TextInput(
        attrs={
        'class':'form-control',
<<<<<<< HEAD
        'placeholder':'Enter your city'
=======
        'placeholder':'Enter your City'
>>>>>>> 6b039926085fcc963503ca6c99f541d840ec82b2
        }
    ))
    upload_passport_image=forms.ImageField(required=True)



    passport_expiry = forms.DateField(required = True,widget=forms.DateInput(
        attrs={
        'class':'form-control',
        'type': 'date',
        'placeholder':'Enter Passport Expiry date'
        }
    ))
    
    
    class Meta:
        model = Customer
<<<<<<< HEAD
        fields = ["passport_id","name","country","phone","address","city","state","rfc","curp","upload_passport_image","passport_expiry"]
=======
        fields = ["passport_id","passport_upload","passport_expiry","name","country","phone","address","city","state","rfc","curp"]
>>>>>>> 6b039926085fcc963503ca6c99f541d840ec82b2


    def clean(self):
 
        super(CustomerCreateForm,self).clean()


        passport_id = self.cleaned_data.get('passport_id') 

        if passport_id:
            if not passport_id.isdigit():
                self._errors['passport_id'] = self.error_class(['Passport Id should be number.'])



                              