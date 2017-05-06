from django.shortcuts import render
from django.views.decorators.cache import cache_page

@cache_page(24 * 60 * 60 * 60)
def home_view(request):
   return render(request, 'index.html');
