from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from .models import Products, Variations, Category
from django.db.models import Q
from .forms import VariationInventoryForm, VariationInventoryFormSet
from django.contrib import messages
from .mixins import StaffRequiredMixin, LoginRequiredMixin

class CategoryListView(ListView):
	model=Category

class CategoryDetailView(DetailView):
	model=Category
	queryset=Category.objects.all()






class ProductDetailView(DetailView):
	model=Products
	queryset=Products.objects.all()

	def get_context_data(self, **kwargs):
		context=super(ProductDetailView, self).get_context_data(**kwargs)
		instance=self.get_object()
		context['related']=Products.objects.get_related(instance)
		return context


	


class ProductListView(ListView):
	model=Products
	queryset=Products.objects.all()
	
	def get_context_data(self,**kwargs):
		context=super(ProductListView, self).get_context_data(**kwargs)
		context['query']=self.request.GET.get("q")
		return context

	def get_queryset(self,**kwargs):
		qs=super(ProductListView, self).get_queryset(**kwargs)
		query=self.request.GET.get("q")
		if query:
			qs=self.model.objects.filter(
				Q(title__icontains=query)
				)
		return qs

		

class VariationListView(ListView):
	model=Variations
	queryset=Variations.objects.all()
	
	def get_context_data(self,**kwargs):
		context=super(VariationListView, self).get_context_data(**kwargs)
		context['formset']=VariationInventoryFormSet(queryset=self.get_queryset())
		

		return context

	def get_queryset(self,**kwargs):
		product_pk=self.kwargs.get("pk")
		if product_pk:
			product=get_object_or_404(Products, pk=product_pk)
			queryset=Variations.objects.filter(product=product)
		return queryset

	def post(self, request, *args, **kwargs):
		formset= VariationInventoryFormSet(request.POST , request.FILES)
		if formset.is_valid():
			formset.save(commit=False)
			for form in formset:
				new_form=form.save(commit=False)

				product_pk=self.kwargs.get("pk")
				product=get_object_or_404(Products, pk=product_pk)
				new_form.product=product
				new_form.save()


			return redirect("product_list_function")

	

#def product_view_func(request, id):
   # template='products/product_detail.html'
    #product_instance=Products.objects.get(id=id)
    #context={
    #'object':product_instance 
    #}
	#return render(request, template, context)


# Create your views here.
