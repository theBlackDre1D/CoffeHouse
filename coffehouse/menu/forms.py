from django import forms
from ..orders.models import Order


class NewOrder(forms.ModelForm):
    note = forms.CharField(widget=forms.Textarea(), max_length=255)
    food_name = forms.CharField(widget=forms.TextInput())
    quantity = forms.DecimalField(widget=forms.NumberInput())

    class Meta:
        model = Order
        fields = ['food_name', 'note', 'quantity']
