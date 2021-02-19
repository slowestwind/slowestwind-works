from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
# import paginator to paginate our page
from django.core.paginator import Paginator

# Create your views here.
# this functin will be executed if user visited on home link.
def home(request):
	return render(request, 'home/index.html')

