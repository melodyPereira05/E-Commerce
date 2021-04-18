from django.shortcuts import render,get_object_or_404,redirect
from product.models import Product,Contact,Category
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Q
from . implementation import prepare_image,predict,get_image,get_colors
from .scrapeData import amazon_scrape,koovs_scrape
import PIL




# Create your views here.
def index(request):
    products=Product.objects.all()
    category=Category.objects.all()
    
    context={
        'products':products,
        'category':category
        
    }
    print(products)
    
    return render(request,'index.html', context)

def allproducts(request):
    products=Product.objects.all()
    context={
        'products':products,
        'count':len(products)
    }
    return render(request,'all-products.html',context)

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
                [email,'melodypereira05@gmail.com'],
        )
        
       
        
        messages.add_message(request, messages.SUCCESS, 'Your query has been submitted,we will get back to you soon')
        
        
        return redirect('accounts:dashboard-profile')
    
    product=Product.objects.all()
    context={'product':product}
        
    return render(request,'contact.html',context)
   


def product_detail(request,product_id):
    prod_detail=get_object_or_404(Product,
                          id=product_id
        )
    print(product_id)
    
    context={
        "product":prod_detail,
    }
    return render(request,'product-detail.html',context)



def search(request):
    filter_category=Product.objects.all()    
    if 'search_query' in request.GET:
        search_box=request.GET['search_query']
        if search_box:
            filter_category=filter_category.filter(
                                                    Q(title__icontains=search_box)|
                                                    Q(description__icontains=search_box)|        
                                                    
                                                    Q(detail__icontains=search_box)| 
                                                    Q(keywords__icontains=search_box)
                                                    )
   
    filter_category = list(filter_category)
    
    context={
        
        'filters':filter_category,
        'count':len(filter_category),
        
        
    }
    return render(request,'searchprod.html',context)


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile'] 
       
        result= prepare_image(myfile)         
        predictlist=predict(result)
        
        image_colors=get_colors(get_image(myfile), 2, True)
        
       
        COLORS = {
        'green': [0,255,0],
        'blue': [0,0,255],
        'yellow': [255, 255, 0],
        'red': [255, 0, 0],
        'orange': [255, 69, 0],
        'black': [0, 0, 0],
        'light+green': [0,255,0],
        'maroon': [128,0,0],
        'dark+red': [139,0,0],
        'brown': [165,42,42],
        'blue': [135,206,250],
        'aqua': [0,255,255],
        'magenta': [255,0,255],
        #'gray': [128,128,128],
        'pink': [255,105,180],
        'purple': [128,0,128],
        'yellow': [218,165,32],


}
 
       
        
              
        colorlists=[]
       
        for name,color in COLORS.items():
            
            col1,col2,col3 =abs(round(image_colors[0][0])-color[0]) ,abs(round(image_colors[0][1])-color[1]) ,abs(round(image_colors[0][2])-color[2])
            print(name,col1,col2,col3)

            # if(col1<200 and col2 <200 and col3<200):
            if(col1<100 and col2<100 and  col3 <100) :

                colorlists.append(name)
                
        for name,color in COLORS.items():
            
            col1,col2,col3 =abs(round(image_colors[1][0])-color[0]) ,abs(round(image_colors[1][1])-color[1]) ,abs(round(image_colors[1][2])-color[2])
            print(name,col1,col2,col3)

            # if(col1<200 and col2 <200 and col3<200):
            if(col1<100 and col2<100 and  col3 <100) :

                colorlists.append(name)
                
        
                
        if 'white' in colorlists:
            colorlists.remove('white')
        if 'snow' in colorlists:
            colorlists.remove('snow')
        if 'whitesmoke' in colorlists: 
            colorlists.remove('whitesmoke')

        print(colorlists)
        print(predictlist)
        amazon=amazon_scrape(colorlists,predictlist)
        koovs=koovs_scrape(colorlists,predictlist)
        # hm=hm_scrape(colorlists,predictlist)
        # zolando=zolando_scrape(colorlists,predictlist)
        
        
        
        
        context={
            'amazon':amazon,
            'koovs':koovs,
            # 'hm':hm,
            # 'zolando':zolando,
            
        }
        
        return render(request,'scrape_product.html',context)
    return render(request,'simple_upload.html')


