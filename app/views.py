from django.shortcuts import render
from .models import Order
from django.db.models import Q

def home(request):

    return render(request, 'index.html')   

def about(request):

    return render(request, 'about.html')   

def services(request):

    return render(request, 'services.html')   

def zakaz(request):
    if 'q' in request.GET:
        q = request.GET['q']
        articles = Order.objects.filter(Q(product_id=q))

    else:
        articles = None
        q = None
    

    return render(request, 'zakaz.html', {"articles":articles, 'q':q})     

def service_details(request):

    return render(request, 'service-details.html')   

def sample_inner_page(request):

    return render(request, 'sample-inner-page.html')   

def pricing(request):

    return render(request, 'pricing.html')   

def get_a_quote(request):

    return render(request, 'get-a-quote.html')   





