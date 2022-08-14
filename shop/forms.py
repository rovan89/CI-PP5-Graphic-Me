from django.forms import ModelForm

from .models import Order



class OrderForm(ModelForm):
    class Meta:
        model = Order

        fields = (
            'id',
            'category',
            'description',
            'number_of_concepts',
            'image',
            'grand_total',
        )