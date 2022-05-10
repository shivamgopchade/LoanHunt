from django import forms
from .models import bank_profile

class BankProfileform(forms.ModelForm):

    class Meta:
        model=bank_profile
        fields=['Aadhar','Pan','Salary','Bank','CTC']

class BankProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = bank_profile
        fields = ['Aadhar','Pan','Salary']


