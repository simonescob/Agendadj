from django.shortcuts import render

# Create your views here.
def index(request):
	data = {"name":"Simon"}
	return render(request, "Contacts/index.html", data)