from django import forms
from .models import Variations
from django.forms import modelformset_factory
class VariationInventoryForm(forms.ModelForm):
	class Meta:
		model=Variations
		fields=[
			"title",
			"price",
			"sale_price",
			"active",
		]

VariationInventoryFormSet=modelformset_factory(Variations, form= VariationInventoryForm, extra=0)