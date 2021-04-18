from django.shortcuts import render
from django.http import HttpResponse
from listings .choices import price_choices,state_choices,bedrooms_choices
from listings.models import Listing
from realtors.models import Realtor



def index(request):
    list=Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    con={'list2':list,
        'state_choices':state_choices,
        'bedrooms_choices':bedrooms_choices,
         'price_choices':price_choices
         }
    return  render(request,'pages/index.html',con )



def about (request):

    #get realtors
    realtors=Realtor.objects.order_by('-hire_date' )
    #get mvp
    mvp_realtor=Realtor.objects.all().filter(is_mpv=True)

    con={
        'realtors1':realtors,
        'mvp_realtor':mvp_realtor

    }
    return  render(request,'pages/about.html',con)
