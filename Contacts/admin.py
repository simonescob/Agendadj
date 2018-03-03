from django.contrib import admin
from .models import Contact

# Register your models here.
# class ContactsAdmin(admin.ModelAdmin):

admin.site.register(Contact)
