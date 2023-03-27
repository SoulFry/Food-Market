from django import forms
from .models import *


class CafeAddForm(forms.ModelForm):
    email = forms.EmailField(label='Почта для заказов',
                             widget=forms.EmailInput(attrs={'class': 'form-title', 'placeholder': 'example@email.com'}))

    class Meta:
        model = Cafe
        fields = ['name', 'description', 'category', 'email', 'location','image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-title', 'placeholder': 'Кафе...'}),
            'description': forms.Textarea(
                attrs={'class': 'form-description', 'placeholder': 'Наше кафе...', 'cols': 90, 'rows': 10}),
        }

        labels = {
            'name': 'Название',
            'description': 'Описание',
            'image': 'Загрузите файл',
            'category': 'Категория',
            'email': 'Почта для связи',
            'location': 'Место нахождение'
        }


class CafeMenuAddForm(forms.ModelForm):

    class Meta:
        model = CafeMenu
        fields = ['name', 'ingredients', 'category', 'cost', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-title', 'placeholder': 'Блюдо...'}),
            'ingredients': forms.Textarea(
                attrs={'class': 'form-description', 'placeholder': 'Это блюдо состоит из...', 'cols': 90, 'rows': 10}),
        }

        labels = {
            'name': 'Название',
            'ingredients': 'Состав',
            'image': 'Загрузите изображение',
            'cost': 'Цена',
            'category': 'Категория'
        }


class CafeMenuCostEdit(forms.ModelForm):

    class Meta:
        model = CafeMenu
        fields = ['cost']

        labels = {
            'cost': 'Цена'
        }