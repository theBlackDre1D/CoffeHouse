from django import forms
from ..orders.models import Order


class NewOrder(forms.ModelForm):
    # food_name = forms.CharField(widget=forms.TextInput())
    menu_number = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)])
    quantity = forms.DecimalField(widget=forms.NumberInput())
    note = forms.CharField(widget=forms.Textarea(), max_length=400)

    class Meta:
        model = Order
        fields = ['menu_number', 'quantity', 'note']
