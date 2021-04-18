from django.shortcuts import get_object_or_404,render
from .models import Listing
from .choices import price_choices,state_choices,bedrooms_choices
from .models import Listing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# Create your views here.

def index(request):
    list1=Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator=Paginator(list1,6)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
    con={'list1': paged_listings}

    return render(request, 'listings/listings.html',con)

def listing(request,listing_id):
    list= get_object_or_404(Listing,pk=listing_id)

    con={ 'list1':list}
    return render(request, 'listings/listing.html',con)

def search(request):

    query_set=Listing.objects.order_by('-list_date')
    #keyword
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_set = query_set.filter(description__icontains=keywords)
    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_set = query_set.filter(city__iexact=city)

   # city
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
          query_set = query_set.filter(state__iexact=state)

    con={
        'state_choices':state_choices,
        'price_choices':price_choices,
        'bedrooms_choices':bedrooms_choices,
        'list1':query_set

        }

    return render(request, 'listings/search.html',con)