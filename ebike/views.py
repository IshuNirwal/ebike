from django.shortcuts import render,redirect
from .models import *
from django.core.mail import send_mail

def Dealer(request):
    if request.method == 'POST':
        # Extract data from the POST request
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        state = request.POST.get('state')
        business = request.POST.get('business')
        firm_name = request.POST.get('firm_name')
        gst = request.POST.get('gst')
        message = request.POST.get('message')
        
        # Create a new instance of DealerEnquiry model
        dealer_enquiry = DealerEnquiry(
            name=name,
            contact=contact,
            email=email,
            city=city,
            pincode=pincode,
            state=state,
            business=business,
            firm_name=firm_name,
            gst=gst,
            message=message
        )
        
        dealer_enquiry.save()
       
        return redirect('thankyou')
    return render(request,'dealer.html')

def Contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        question = request.POST.get('question')

        # Save the contact enquiry to the database
        contact_enquiry = ContactEnquiry.objects.create(
            name=name,
            email=email,
            question=question
        )
        contact_enquiry.save()

        # Send email notification
        send_mail(
            'New Contact Enquiry',
            f'Name: {name}\nEmail: {email}\nQuestion: {question}',
            "nirwalriya51@gmail.com",  
            ['ishnirwal@gmail.com'], 
            fail_silently=False,
        )

        return redirect('thankyou') 

    return render(request, 'contact.html')

def Home(request):
    return render(request,'index.html')

def Thank(request):
    return render(request,'thankyou.html')

def Skylark(request):
    return render(request,'skylark.html')

def Swallow(request):
    return render(request,'swallow.html')

def Starling(request):
    return render(request,'starling.html')

def Canary(request):
    return render(request,'canary.html')

def Eagle(request):
    return render(request,'eagle.html')

def Drake(request):
    return render(request,'drake.html')

def Models(request):
    return render(request,'models.html')

def About(request):
    return render(request,'about.html')


