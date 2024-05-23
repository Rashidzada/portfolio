from django.shortcuts import render
from .import models
# Create your views here.
def index(request):
    context = {
        'userprofiles':models.UserProfile.objects.all(),
        
    }
    return render(request,'index.html',context)



def portfolio_details(request):
    return render(request,'portfolio_details.html')



def test(request):
    userprofiles = models.UserProfile.objects.all()
    context = {
        'userprofiles':userprofiles,
        
    }
    return render(request,'test.html',context)