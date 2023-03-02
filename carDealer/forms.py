from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.db import models  
from django.forms import fields  
from .models import Item  
from django import forms  

# class UserRegistrationForm(UserCreationForm):
#     fast = forms.CharField(max_length=101)
#     last_name = forms.CharField(max_length=101)
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'fast', 'last_name', 'email', 'password1', 'password2']

class UserImage(forms.ModelForm): 

    #  make = forms.CharField(
    #      label='',
    #      max_length=200,
    #      required=False,
    #      widget=forms.TextInput(attrs={'class': 'col-lg-6 col-md-6 col-sm-6' , 'placeholder': 'Make', 'style': 'margin-top: 50px; width: 300px;  border-radius: 10px; background: #f1f1f1;'})

    #  )
    #  year = forms.CharField(
    #      label='',
    #      max_length=200,
    #      required=False,
    #      widget=forms.TextInput(attrs={'class': 'col-lg-9 col-md-9 col-sm-9' ,'placeholder': 'Year', 'style': 'width: 300px;  border-radius: 10px; background: #f1f1f1;'})

    #  )
    #  model = forms.CharField(
    #      label='',
    #      max_length=200,
    #      required=False,
    #      widget=forms.TextInput(attrs={'class': 'col-lg-6 col-md-6 col-sm-6','placeholder': 'Model', 'style': 'width: 300px;  border-radius: 10px; background: #f1f1f1;'})

    #  )
    #  suspension = forms.CharField(
    #      label='',
    #      max_length=200,
    #      required=False,
    #      widget=forms.TextInput(attrs={'placeholder': 'Suspension', 'style': 'width: 300px;  border-radius: 10px; background: #f1f1f1;'})

    #  )
    #  baseprice = forms.IntegerField(
    #      label='',
    #      required=False,
    #      widget=forms.TextInput(attrs={'placeholder': 'Baseprice', 'style': 'width: 300px;  border-radius: 10px; background: #f1f1f1;'})

    #  )
    #  buyitnow = forms.IntegerField(
    #      label='',
    #      required=False,
    #      widget=forms.TextInput(attrs={'placeholder': 'Buy Now', 'style': 'width: 300px;  border-radius: 10px; background: #f1f1f1;'})

    #  )
     
    #  status = forms.CharField(
    #      label='',
    #      max_length=200,
    #      required=False,
    #      widget=forms.TextInput(attrs={'placeholder': 'Status', 'style': 'width: 300px;  border-radius: 10px; background: #f1f1f1;'})

    #  )
    #  start_date = forms.CharField(
    #      label='',
    #      max_length=200,
    #      required=False,
    #      widget=forms.TextInput(attrs={'placeholder': 'Bid end Date', 'style': 'width: 300px;  border-radius: 10px; background: #f1f1f1;'})

    #  )
    #  start_date = forms.DateTimeField()
    #  start_date = forms.CharField(
    #      label='',
    #      max_length=200,
    #      required=False,
    #      widget=forms.TextInput(attrs={'placeholder': 'Bid end Date', 'style': 'width: 300px;  border-radius: 10px; background: #f1f1f1;'})

    #  )
     profile = forms.ImageField(
        label='',
        
     )
    
    #  sold = forms.CharField(
    #      max_length=200,
    #      required=False,

    #  ) 

     class Meta:  
        # To specify the model to be used to create form  
        model = Item  
        # It includes all the fields of model  
        # fields = '__all__'  
        fields = ['id' , 'make' , 'year' ,  'model' ,'suspension' , 'baseprice' ,'buyitnow' , 'status','start_date', 'profile']

        
# class ManufacturerForms(forms.ModelForm):
#      billingtype = forms.CharField(
#         max_length=200,
#         required=False,
#      )
#      materialtype = forms.CharField(
#          max_length=200,
#          required=False,

#      )
#      addonstype = forms.CharField(
#          max_length=200,
#          required=False,

#      )
#      addonsnumber = forms.CharField(
#          max_length=200,
#          required=False,

#      )

#      class Meta:
#         model = manufacturer
#         # fields = "__all__"
#         fields = ['id1', 'name' , 'emailid' , 'address' , 'passcode' ,  'billingtype' ,'materialtype' , 'addonstype' , 'addonsnumber' , 'phoneno' ]