from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class MiFormularioDeCreacionDeUsuarios(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Password', widget=forms.PasswordInput)
    passowrd2 = forms.CharField(label = 'Repeat Password', widget=forms.PasswordInput)
    
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k: "" for k in fields}



class  MiFormularioDeEdicionDeDatosDeUsuarios(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label = 'Name', max_length= 20)
    last_name = forms.CharField(label = 'Last Name', max_length= 20)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name','avatar']