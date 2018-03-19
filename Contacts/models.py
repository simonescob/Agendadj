from django.db import models

# Create your models here.
class Contact(models.Model):
	fname = models.CharField(max_length=150)
	lname = models.CharField(max_length=150)
	phone = models.IntegerField()
	email = models.EmailField(unique=True)

	def __str__(self):
		return self.fname


