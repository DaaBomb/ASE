from django.shortcuts import render,HttpResponse,redirect
from accounts.forms  import(
 RegistrationForm,
EditProfileForm,customreg , ChangeProfileForm)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import UserProfile
# Create your views here.

@login_required
def home(request):
    return render(request,'accounts/home.html')
def register(request):
     if request.method=='POST':
         form1=RegistrationForm(request.POST)
         form=customreg(request.POST)
         if form1.is_valid():
             form1_instance=form1.save()
             form_instance=form.save(commit=False)

             form_instance.user=form1_instance

             form_instance.save()

             return redirect('/accounts')
         else:
             return HttpResponse("form 1 is invalid")

     else:
         form=customreg()
         form1=RegistrationForm()
         args={'form':form,'form1':form1}
         #print(args[])
         return render(request,'accounts/reg_form.html',args)


@login_required
def view_profile(request):
    args={'user':request.user}
    return render(request,'accounts/profile.html',args)


@login_required
def edit_profile(request):        #edit profile view
    if request.method=='POST':
        form=EditProfileForm(request.POST,instance=request.user)
        form1=ChangeProfileForm(request.POST,instance=request.user)
        #UserProfile.objects.filter(user=request.user).update(description='good_game')
        if form.is_valid() and form1.is_valid():
            form.save()
            UserProfile.objects.filter(user=request.user).update(description=request.POST['description'])
            UserProfile.objects.filter(user=request.user).update(city=request.POST['city'])
            UserProfile.objects.filter(user=request.user).update(phone=request.POST['phone'])
            return redirect('/accounts/profile')
        else:
            return HttpResponse("form  is invalid")

    else:
        form=EditProfileForm(instance=request.user)
        form1=ChangeProfileForm(request.POST,instance=request.user)
        args={'form':form,'form1':form1}
        return render(request,'accounts/edit_profile.html',args)


@login_required
def change_password(request):        #change password view
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/accounts/profile')
        else:
            return redirect('/accounts/change-password')

    else:
        form=PasswordChangeForm(user=request.user)

        args={'form':form}
        return render(request,'accounts/change_password.html',args)
