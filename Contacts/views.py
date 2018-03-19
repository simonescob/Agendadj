from django.shortcuts import redirect, render, get_object_or_404

from .models import Contact
from .forms import CreateContactForm, CreateContactModelForm

def index(request):
	contact = Contact.objects.all()
	if request.method == "POST":
		form = CreateContactModelForm(request.POST)
		if form.is_valid():
			formContact = form.save(commit=False)
			formContact.save()
			print("created!!")
			return redirect("home")
	else:
		form = CreateContactForm()
	data = {
		"contacts": contact,
		"form": form,
	}
	return render(request, "Contacts/index.html", data)

def create(request):
	if request.method == "POST":
		form = CreateContactModelForm(request.POST)
		if form.is_valid():
			formContact = form.save(commit=False)
			formContact.save()
	else:
		form = CreateContactForm()
	data = {
		"form": form,
	}
	return render(request, "Contacts/create.html", data)

def delete(request, contact_id):
	contact = Contact.objects.filter(id=contact_id)
	print("Viewed")
	if request.method == "POST":
		contact.delete()
		return redirect("/")
	return render(request, "Contacts/remove.html")
		
def edit(request, contact_id):
	contact = Contact.objects.get(pk=contact_id)
	print(contact_id)
	form = CreateContactModelForm(request.POST or None, instance=contact)
	if form.is_valid():
		form.save()
		return redirect("/#%s" % contact_id)
	data = {
		"form": form,
	}
	return render(request, "Contacts/edit.html", data)






