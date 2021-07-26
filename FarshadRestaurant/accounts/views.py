from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .models import Clients , Titelrules , Rules
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_register(request):
    titelrules = Titelrules.objects.all()
    statements = Rules.objects.all()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            e = Clients(user=user,
                        first_name=request.POST['first_name'],
                        last_name=request.POST['last_name'],
                         phone=request.POST['phone'],
                        phoneNumber=request.POST['phoneNumber'],
                         address=request.POST['address'])
            e.save()
            login(request, user)
            messages.success(request, 'اطلاعات شما با موفقیت ثبت شد.اکنون میتوانید ثبت سفارش کنید.', 'success')
            return redirect('shop:home')
        else:
            for er in form.error_messages:
                messages.add_message(request, messages.ERROR, er)
    return render(request, 'accounts/register.html', {'form': UserCreationForm(), 'is_valid': True,'titelrules':titelrules,'statements':statements})



def user_login(request):
    if request.POST:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            messages.success(request, 'با موفقیت وارد شدید.اکنون میتوانید سفارش خود را ثبت کنید', 'success')

            return redirect('shop:home')
        else:
            messages.error(request, 'نام کاربری  یا  رمزعبور  اشتباه  است  دوباره  تلاش  کنید.', 'danger')
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'با موفقیت خارج شدید', 'success')
    return redirect('shop:home')



@login_required
def edit_page(request):
    if request.POST:
         username = request.user
         usrid = username.id
         Clients.objects.filter(user_id=usrid).update(address=request.POST['newadd'],phoneNumber=request.POST['newphone'])
         messages.success(request, 'اطلاعات شما با موفقیت ویرایش شد', 'success')
         return redirect('shop:home')
    return render(request,'accounts/editpage.html')





# last
# def user_login(request):
# 	if request.method == 'POST':
# 		form = UserLoginForm(request.POST)
# 		if form.is_valid():
# 			cd = form.cleaned_data
# 			user = authenticate(request, username=cd['username'], password=cd['password'])
# 			if user is not None:
# 				login(request, user)
# 				messages.success(request, 'با موفقیت وارد شدید.اکنون میتوانید سفارش خود را ثبت کنید', 'success')
# 				return redirect('shop:home')
# 			else:
# 				messages.error(request, 'نام کاربری  یا  رمزعبور  اشتباه  است  دوباره  تلاش  کنید.', 'danger')
# 	else:
# 		form = UserLoginForm()
# 	return render(request, 'accounts/login.html', {'form':form})
#
#
# def user_logout(request):
# 	logout(request)
# 	messages.success(request, 'با موفقیت خارج شدید', 'success')
# 	return redirect('shop:home')
#
# def user_register(request):
# 	if request.method == 'POST':
# 		form = UserRegistrationForm(request.POST)
# 		if form.is_valid():
# 			# cd = form.cleaned_data
# 			form.save()
# 			username = form.cleaned_data.get('username')
# 			raw_password = form.cleaned_data.get('password1')
# 			# user = User.objects.create_user(cd['full_name'], cd['username'], cd['password'],cd['mobile'],cd['address'])
# 			# user.save()
# 			user = authenticate(username=username, password=raw_password)
# 			login(request, user)
# 			messages.success(request, 'اطلاعات شما با موفقیت ثبت شد.اکنون میتوانید ثبت سفارش کنید.', 'success')
# 			return redirect('shop:home')
# 	else:
# 		form = UserRegistrationForm()
# 	return render(request, 'accounts/register.html', {'form':form})