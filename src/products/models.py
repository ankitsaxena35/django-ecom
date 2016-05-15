from django.db import models
from django.db.models import signals
from django.core.urlresolvers import reverse
from django.dispatch import receiver
class ProductQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self, *args, **kwargs):
        return self.get_queryset().active()

    def get_related(self, instance):
    	products_one=self.get_queryset().filter(category__in=instance.category.all())
    	products_two=self.get_queryset().filter(default=instance.default)
    	qs=(products_one | products_two).distinct().exclude(id=instance.id)
    	return qs   		


class Products(models.Model):
	title=models.CharField(max_length=200)
	description=models.TextField(blank=True, null=True)
	price=models.DecimalField(decimal_places=2, max_digits=20)
	active=models.BooleanField(default=True)
	category=models.ManyToManyField('Category')
	default=models.ForeignKey('Category', related_name='dafault_category', blank=True, null=True)

	objects=ProductManager()

	def __unicode__(self):
		return self.title

	def get_image_url(self):
		img=self.productimage_set.first()
		if img:
			return img.image.url 
		return img




class Variations(models.Model):
 	product=models.ForeignKey(Products)
 	title=models.CharField(max_length=200)
	price=models.DecimalField(decimal_places=2, max_digits=20)
	sale_price=models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
	active=models.BooleanField(default=True)
	inventory=models.IntegerField(null=True, blank=True)


	def __unicode__(self):
		return self.title
	
	def get_price(self):
		if self.sale_price is not None:
			return self.sale_price 
		else:
		    return self.price	

def post_post_saved_reciever(sender,instance, created, *args, **kwargs):
    product=instance
    variations=product.variations_set.all()
    if variations.count < 1:
    	new_var=Variations()
    	new_var.product=product
    	new_var.title="Default"
    	new_var.price=product.price
    	new_var.save()

signals.post_save.connect(post_post_saved_reciever ,sender=Products)

class ProductImage(models.Model):
	product=models.ForeignKey(Products)
	image=models.ImageField(upload_to='products/')

	def __unicode__(self):
		return self.product.title


class Category(models.Model):
	title=models.CharField(max_length=100, unique=True)
	description=models.TextField(blank=True, null=True)
	slug=models.SlugField(unique=True)
	active=models.BooleanField(default=True)
	timestamp=models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('product_categories',kwargs={"slug":self.slug })	

class ProductFeatured(models.Model):
	product=models.ForeignKey(Products)
	title=models.CharField(max_length=120, blank=True)
	image=models.ImageField(upload_to='featured/')
	background_image=models.BooleanField(default=False)
	text=models.CharField(max_length=120, blank=True, null=True)
	text_right=models.BooleanField(default=False)
	show_price=models.BooleanField(default=True)
	active=models.BooleanField(default=True)
	test_css=models.CharField(max_length=6)

	def __unicode__(self):
		return self.product.title		













