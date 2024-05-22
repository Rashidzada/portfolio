from django.shortcuts import render
from .import models
# Create your views here.
def index(request):
    # context = {
    #     'user':models.UserProfile.objects.get(user = request.user)
    # }
    return render(request,'index.html')



def portfolio_details(request):
    return render(request,'portfolio_details.html')