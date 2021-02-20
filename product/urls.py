from django.urls import path
from  . import views


urlpatterns = [
    path('', views.index , name="home-page"),
    path('contact/',views.contact,name="contact-us" ),
    path('search/',views.search,name="search"),
    path('product/<int:product_id>/',views.product_detail, name="product_detail"),
 
    
]