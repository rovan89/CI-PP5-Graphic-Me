from django.forms import ModelForm
from django import forms

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
            
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {

        }

        