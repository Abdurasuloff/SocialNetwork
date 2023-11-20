from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "password1", "password2"]
        

class MyUserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name",  'bio', "birth_of_date", "profile", "cover",]