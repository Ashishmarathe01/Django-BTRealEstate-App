from django.shortcuts import render,redirect
from .models import Contact
from django.core.mail import send_mail

# Create your views here.
def contact(requset):
    if requset.method=='POST':
        listing_id=requset.POST['listing_id']
        listing = requset.POST['listing']
        name= requset.POST['name']
        email = requset.POST['email']
        phone = requset.POST['phone']
        message = requset.POST['message']
        user_id = requset.POST['user_id']
        realtor_email=requset.POST['realtor_email']

        contact=Contact( listing_id=listing_id,listing=listing,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contact.save()

        ## email inqure made
        send_mail(
            'property listing inquiry',
            'The equirey made'+listing+'ok',
            'tanmaybhosale0007@gamil.com',
            ['ashishmarathe18@gmail.com',realtor_email ],
            fail_silently=False
        )

        ## yor request submitted

    return redirect('/listings/'+listing_id)
