from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from datetime import datetime
from django.utils.safestring import mark_safe
from django.forms import ModelForm
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
# Create your models here.
class Category(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'), 
    )
    parent = TreeForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE) #for subcategory purpose eg : clothing->Tees
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image=models.ImageField(upload_to='photos/category/%Y/%m/%d/',blank=True)
    status=models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    # def get_absolute_url(self):
    #     return reverse('category_detail', kwargs={'slug': self.slug})

    # def __str__(self):                           # __str__ method elaborated later in
    #     full_path = [self.title]                  # post.  use __unicode__ in place of
    #     k = self.parent
    #     while k is not None:
    #         full_path.append(k.title)
    #         k = k.parent
    #     return ' / '.join(full_path[::-1])
    
    
class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    VARIANTS = (
        ('None', 'None'),
        ('Size', 'Size'),
        ('Color', 'Color'),
        ('Size-Color', 'Size-Color'),

    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #one category many products associated with it
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image=models.ImageField(upload_to='photos/products/%Y/%m/%d/',null=False)
    price = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    amount=models.IntegerField(default=0)
    minamount=models.IntegerField(default=3)
    variant=models.CharField(max_length=10,choices=VARIANTS, default='None')
    detail=RichTextUploadingField()  #check the admin area for super fun
    slug = models.SlugField(null=False, unique=True)
    status=models.CharField(max_length=10,choices=STATUS)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


   # use this function to add more image to the product(read only fields cant do anything more than that) -- check admin area for more info
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    # def get_absolute_url(self):
    #     return reverse('category_detail', kwargs={'slug': self.slug})

    # def avaregereview(self):
    #     reviews = Comment.objects.filter(product=self, status='True').aggregate(avarage=Avg('rate'))
    #     avg=0
    #     if reviews["avarage"] is not None:
    #         avg=float(reviews["avarage"])
    #     return avg

    # def countreview(self):
    #     reviews = Comment.objects.filter(product=self, status='True').aggregate(count=Count('id'))
    #     cnt=0
    #     if reviews["count"] is not None:
    #         cnt = int(reviews["count"])
    #     return cnt
    
    
class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,blank=True)
    image = models.ImageField(upload_to='photos/products/%Y/%m/%d/',blank=True)

    def __str__(self):
        return self.title
    
    

class Contact(models.Model):
    
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name= models.CharField(blank=True,max_length=20)
    email= models.CharField(blank=True,max_length=50)
    subject= models.CharField(blank=True,max_length=50)
    message= models.TextField(blank=True,max_length=255)
    status=models.CharField(max_length=10,choices=STATUS,default='New')  #whether the query has been answered or not (generally for the ease of admin)
    user_id=models.IntegerField(blank=True)
    created_at=models.DateTimeField(default=datetime.now,blank=True)
    updated_at=models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.name

