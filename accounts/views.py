from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from contacts.models import Contact
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                # SAME USERNAM
                return redirect('reg')

            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'testing done')

                    return redirect('reg')
                else:
                    #look good
                    user=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
                    user.save();
                    # user created
                    return redirect('login')
        else:
            #doesnot match
            return redirect('reg')
    else:
        return render(request,'accounts/register.html')


def logout(request):
    if request.method=='POST':
        auth.logout(request)
        #ur log out

        return redirect('index')

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            #succefully login
            return redirect('dashboard')
        else:
            # not user
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def dashboard(request):
    user_contact=Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context={
        'contacts':user_contact
    }


    return render(request,'accounts/dashboard.html',context)