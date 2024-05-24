from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .import models
from .models import Contact
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

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            messages.warning(request,'Try agian password or username incorrect')
            return redirect('admin:index')
    return render(request,'login_view.html')




def contact(request):
    if request.method == 'POST':
        try:
            # Extract form data
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            # Create and save the contact instance
            contact = Contact(name=name, email=email, subject=subject, message=message)
            contact.save()

            # Success message
            messages.success(request, "Your message has been sent successfully!")
            return redirect('thankyou')
        except Exception as e:
            # Log the error if necessary (e.g., with logging module)
            # Error message for the user
            messages.error(request, "An error occurred while sending your message. Please try again.")
    else:
        # Warning message if the request method is not POST
        messages.warning(request, "Your message request was not sent. Please try again using the form.")

    return render(request, 'contact.html')


def thankyou(request):
    return render(request,'thankyou.html')