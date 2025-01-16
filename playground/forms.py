from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'email', 'password1', 'password2']
