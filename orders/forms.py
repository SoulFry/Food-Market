from django import forms


class AdressSubmitForm(forms.Form):
    adress = forms.CharField(label='Адресс', widget=forms.TextInput(
        attrs={'class': 'form-title', 'placeholder': 'Страна, Город, Улица, Номер дома, Подъезд, Номер Квартиры'}))
    time = forms.DateTimeField(label='Дата и время', widget=forms.DateTimeInput(
        attrs={'placeholder': '2023-12-31 23:59'}
    ))

