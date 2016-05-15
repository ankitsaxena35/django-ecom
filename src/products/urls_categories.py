from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from .views import CategoryListView, CategoryDetailView
urlpatterns=[
  url(r'^(?P<slug>[\w-]+)$', CategoryDetailView.as_view(), name='product_categories'),
  url(r'^$', CategoryListView.as_view(), name='category_list_function'),
]