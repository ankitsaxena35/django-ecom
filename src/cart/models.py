from django.db import models
from django.conf import settings
from products.models import Variations
from django.core.urlresolvers import reverse

class CartItem(models.Model):
	cart=models.ForeignKey("Cart")
	item=models.ForeignKey(Variations)
	quantity=models.PositiveIntegerField(default=1)

	def __unicode__(self):
		return self.item.title

	def remove(self):
		return "%s?item=%s&delete=True" %(reverse("cart"), self.item.id)



class Cart(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL, null=True ,blank=True)
	items=models.ManyToManyField(Variations , through=CartItem)
	timestamp=models.DateTimeField(auto_now_add=True, auto_now=False)
	update=models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return str(self.id)


# Create your models here.
