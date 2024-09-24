from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

# def homeView(request):
#     message = ' hello world'

#     return HttpResponse(message) # returning httpresponse object 

class homeView(TemplateView):
        template_name ='index.html'



class aboutView(TemplateView):
        template_name = 'about.html'

class contactView(TemplateView):
        template_name = 'contact.html'

class cartView(TemplateView):
        template_name = 'cart.html'
