from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

# def homeView(request):
#     message = ' hello world'

#     return HttpResponse(message) # returning httpresponse object 

class homeView(TemplateView):
        template='index.html'



def aboutView(request):
        message = 'this is about section of our project'

        return HttpResponse(message)

def contactView(request):
        message = 'this is the contact section of the page'

         
        return HttpResponse(message)

def cartView(request):
        message = 'this is the cart section of the page'
       
        
        return HttpResponse(message)
