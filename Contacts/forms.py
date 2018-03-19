from django import forms
from .models import Contact

class CreateContactForm(forms.Form):
	fname = forms.CharField(label="First Name")
	lname = forms.CharField(label="Last Name")
	phone = forms.IntegerField(label="Phone")
	email = forms.EmailField(label="Email")

	def clean_email(self):
		email = self.cleaned_data["email"]
		contactEmail = Contact.objects.filter(email=email).exists()
		if contactEmail:
			raise forms.ValidationError("Exist a email with this name, please try with other.")
		return email

class CreateContactModelForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = "__all__"

		labels = {
			"fname": "First Name", 
			"lname": "Last Name",
		}

		widgets = {
			"name": forms.TextInput(attrs={})
		}

	# def clean_email(self):
	# 	email = self.cleaned_data["email"]
	# 	contactEmail = Contact.objects.filter(email=email).exists()
	# 	if contactEmail:
	# 		raise forms.ValidationError("Exist a email with this name, please try with other.")
	# 	return email

