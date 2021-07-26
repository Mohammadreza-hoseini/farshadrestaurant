from django.shortcuts import render , get_object_or_404
from .models import Category, Product , Masterchef , Info , Slider , Aboutus , Aboutusparag
from cart.forms import CartAddForm
# Create your views here.
def home(request):
    proposals = Masterchef.objects.all()
    informations = Info.objects.all()
    sliders = Slider.objects.all()
    return render(request,'shop/home.html',{'proposals':proposals,'informations':informations,'sliders':sliders})

def aboutus(request):
    aboutsus = Aboutus.objects.all()
    aboutusparags = Aboutusparag.objects.all()
    return render(request,'shop/aboutus.html',{'aboutsus':aboutsus,'aboutusparags':aboutusparags})


def contactus(request):
    return render(request,'shop/contactus.html')

def menu(request,slug=None):
    products = Product.objects.filter(available=True)
    categories = Category.objects.filter(is_sub=False)
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)
    return render(request, 'shop/menu.html', {'products': products, 'categories': categories})


def product_detail(request, slug):
	product = get_object_or_404(Product, slug=slug)
	form = CartAddForm()
	return render(request, 'shop/product_detail.html', {'product':product, 'form':form})

