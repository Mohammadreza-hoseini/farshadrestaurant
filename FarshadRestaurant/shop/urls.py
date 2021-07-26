from django.urls import path
from . import views


app_name = 'shop'
urlpatterns = [

	path('menu/', views.menu, name='menu'),
	path('aboutus/',views.aboutus,name='aboutus'),
	path('contactus/',views.contactus,name='contactus'),
	path('<slug:slug>/', views.product_detail, name='product_detail'),
	path('category/<slug:slug>/', views.menu, name='category_filter'),
  	path('', views.home, name='home'),
]