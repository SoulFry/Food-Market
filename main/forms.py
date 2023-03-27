from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

from .models import *

User = get_user_model()

class UserRegistration(UserCreationForm):
    email = forms.EmailField(label= 'Адресс почты', widget=forms.EmailInput(attrs={'class': "auth-input", 'placeholder': 'example@email.com'}))
    password1 = forms.CharField(label='Пароль',min_length=8, widget=forms.PasswordInput(attrs={'class': "auth-input", 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повторите пароль',min_length=8, widget=forms.PasswordInput(attrs={'class': "auth-input", 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

class UserAvatarChange(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar']

        labels = {
            'avatar': 'Загрузите аватар'
        }


class UserLogin(AuthenticationForm):
    username = forms.EmailField(label='Адресс почты', widget=forms.EmailInput(attrs={'class': "auth-input", 'placeholder': 'example@email.com'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': "auth-input", 'placeholder': 'Пароль'}))


class PasswordCheck(forms.Form):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput(attrs={'class':"auth-input", 'placeholder': 'Введите старый пароль'}))


class PasswordChange(forms.Form):
    new_password = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'class':"auth-input", 'placeholder': 'Введите новый пароль'}))
    new_password2 = forms.CharField(label='Повторите новый пароль', widget=forms.PasswordInput(attrs={'class': "auth-input", 'placeholder': 'Повторите новый пароль'}))


class EmailCheck(forms.Form):
    email = forms.EmailField(label='Укажите вашу почту', widget=forms.EmailInput(attrs={'class': 'auth-input', 'placeholder': 'example@email.com'}))


class CommentForm(forms.ModelForm):
    subject = forms.CharField(max_length=200, label='Тема')

    class Meta:
        model = CommentCafe
        fields = ['subject', 'comment', 'mark']

        widgets = {
            'comment': forms.Textarea(attrs={'cols': 100, 'rows': 12, 'placeholder': 'Ваш Отзыв'})
        }

        labels = {
            'mark': 'Оценка',
            'comment': 'Отзыв',
        }

