from django import forms
from ..orders.models import Order, Drink


class NewOrder(forms.ModelForm):
    DRINK_LIST = Drink.objects.all()
    # food_name = forms.CharField(widget=forms.TextInput())
    menu_number = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)])
    # quantity = forms.DecimalField(widget=forms.NumberInput())
    note = forms.CharField(widget=forms.Textarea(), max_length=400)
    drink = forms.Select(choices=DRINK_LIST)

    class Meta:
        model = Order
        fields = ['menu_number', 'drink', 'note']

