from django import forms


class CartAddProduct(forms.Form):
    count = forms.IntegerField(min_value=1, max_value=10, step_size=1, label='Количество', initial=1,
                               widget=forms.NumberInput(attrs={'class': 'count-choice'}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    class Meta:
        widget = {
            'count': forms.NumberInput(attrs={'class': 'count-choice'})
        }
