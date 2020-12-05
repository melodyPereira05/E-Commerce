from django.shortcuts import render,get_object_or_404,redirect
from product.models import Product,Contact
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def index(request):
    products=Product.objects.all()
    
    context={
        'products':products
    }
    print(products)
    
    return render(request,'index.html', context )

def contact(request):
   
    
    if request.method =='POST':
        
        name=request.POST['name']
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        user_id=request.POST['user_id']
      
        
        
        if request.user.is_authenticated:
            user_id=request.user.id
        
            
        
        contact=Contact(name=name,email=email,subject=subject,message=message,user_id=user_id)
        
        contact.save()
        #sending email
        send_mail(
            subject,
                message,
                'melzpereira0509@gmail.com',
                [email,'melodypereira05@gmail.com'],#'sukhadamorgaonkar28@gmail.com','chetna.nihalani@yahoo.in'],
        )
        
       
        
        messages.add_message(request, messages.SUCCESS, 'Your query has been submitted,we will get back to you soon')
        
        
        return redirect('accounts:dashboard-profile')
    
    product=Product.objects.all()
    context={'product':product}
        
    return render(request,'contact.html',context)
   


def product_detail(request,product_id):
    return render(request,'product-detail.html')