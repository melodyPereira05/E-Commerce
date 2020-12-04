from django.shortcuts import render
from product.models import Product

# Create your views here.
def index(request):
    products=Product.objects.all()
    
    context={
        'products':products
    }
    print(products)
    
    return render(request,'index.html', context )

def contact(request):
    return render(request,'contact.html')