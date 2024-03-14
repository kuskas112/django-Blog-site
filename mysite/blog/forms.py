from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from blog.models import Comments


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.TextInput(attrs={'class':'form-input'}))

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class':'form-input'}))

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='Логин', widget=forms.Textarea(attrs={'rows': 4}))
    class Meta:
        model = Comments
        fields = ('content',)