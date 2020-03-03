from django import forms
from .models import Product
from .models import Collection


class ProductCreationForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['name', 'photo', 'description']


class CollectionCreationForm(forms.ModelForm):
	class Meta:
		model = Collection
		fields = ['name', 'products']
