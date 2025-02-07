from django import forms

class UserForm(forms.Form): #creating a form class
    name = forms.CharField(label="Name", max_length=100) #adding a name field to the form
    # Adding a password field to the form
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
