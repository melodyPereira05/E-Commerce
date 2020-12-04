from django.contrib import admin
from product.models import Category,Product,Images

#https://docs.djangoproject.com/en/3.1/ref/contrib/admin/


class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','parent','status']
    list_filter=['status']
    
class ProductImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 3
    
class ProductAdmin(admin.ModelAdmin):
    list_display=['title','category','status','image_tag']
    list_filter=['category']
    readonly_fields=('image_tag',)
    inlines = [ProductImageInline]
    

 
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images)   