from .models import Contact
from django import forms

class Create_Contact(forms.ModelForm):
    #username = forms.CharField(required = False,widget=forms.TextInput(attrs={"disabled":True}))
    contactname = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-control-sm"}))
    number = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-control-sm", "type" :"number"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-control-sm", "type" :"email"}))
    address = forms.CharField(widget = forms.Textarea(attrs={"class":"form-control form-control-sm", "rows":5}))

    class Meta:
        model = Contact
        fields =[
            'contactname','number','email','address'
        ]