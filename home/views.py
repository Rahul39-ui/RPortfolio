from django.shortcuts import render
from home.models import Card

from home.models import project
# Create your views here.
def index(request):

    objects = Card.objects.all() 
    objects_p = project.objects.all()   
    
    context = {
        'cards': objects,
        'projects': objects_p
    }
    
    return render(request, 'index.html', context)

