from django.contrib import admin

from .models import Products, Variations, ProductImage, Category, ProductFeatured
class VariationInline(admin.TabularInline):
	model=Variations
	extra=1

class ProductImageInline(admin.TabularInline):
	model=ProductImage
	extra=1


class ProductInline(admin.ModelAdmin):
	list_display=['__unicode__', 'price']
	inlines=[
		VariationInline,
		ProductImageInline
	]
	class Meta:
		model=Products

admin.site.register(Products, ProductInline)
#admin.site.register(Variations)
#admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(ProductFeatured)
# Register your models here.

