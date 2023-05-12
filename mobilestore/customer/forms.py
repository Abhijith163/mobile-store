from django import forms
from .models import CartItem

class CartItemForm(forms.ModelForm):
    quantity = forms.IntegerField(initial=1, min_value=1, max_value=100)

    class Meta:
        model = CartItem
        fields = ('product', 'quantity')


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=10, initial=1, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity...'}))