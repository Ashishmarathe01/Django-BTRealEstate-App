from django.contrib import admin

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','tittle','is_published','price','list_date')
    list_display_links = ('id','tittle')
    list_filter = ('id','tittle')
    list_editable = ('is_published',)
    search_fields = ('id','tittle','price','state')
    list_per_page = 25
from .models import Listing
admin.site.register(Listing,ListingAdmin)
