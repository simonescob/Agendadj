from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="home"),
	path('all', views.index),
	path('create', views.create, name="create"),
	path('delete/<int:contact_id>', views.delete, name="delete"),
	path('edit/<int:contact_id>', views.edit, name="edit"),
]