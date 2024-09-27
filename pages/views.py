from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# def homeView(request):
#     message = ' hello world'

#     return HttpResponse(message) # returning httpresponse object 

class HomeView(TemplateView):
        template_name ='index.html'



# class aboutView(TemplateView):
#         template_name = 'about.html'

def aboutView(request):
        return render(request,'about.html')
class ContactView(TemplateView):
        template_name = 'contact.html'

class CartView(TemplateView):
        template_name = 'cart.html'
