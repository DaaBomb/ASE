from django.shortcuts import render,HttpResponse,redirect
from accounts.forms  import(
 RegistrationForm,customregcompany,
 regcompany,regteam,
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
             if request.POST['Jobtitle'] != 'CEO':
                 form1_instance=form1.save()
                 form_instance=form.save(commit=False)

                 form_instance.user=form1_instance

                 form_instance.save()

                 return redirect('/accounts')
             else:
                 return HttpResponse("CEO should register with company ")
         else:
             return HttpResponse("form 1 is invalid")

     else:
         form=customreg()
         form1=RegistrationForm()
         args={'form':form,'form1':form1}
         #print(args[])
         return render(request,'accounts/reg_form.html',args)

def registercompany(request):
     if request.method=='POST':
         form1=RegistrationForm(request.POST)
         form=customregcompany(request.POST)
         form2=regcompany(request.POST)
         if form1.is_valid() and form.is_valid() and form2.is_valid():

             if request.POST['Jobtitle'] == 'CEO':
                 form2_instance=form2.save()
                 form1_instance=form1.save()
                 form_instance=form.save(commit=False)

                 form_instance.user=form1_instance
                 form_instance.company_name=form2_instance

                 form_instance.save()

                 return redirect('/accounts')
             else:
                 return HttpResponse("only ceo can register ")
         else:
             return HttpResponse("form 1 is invalid")

     else:
         form=customregcompany()
         form1=RegistrationForm()
         form2=regcompany()
         args={'form':form,'form1':form1,'form2':form2}
         #print(args[])
         return render(request,'accounts/reg_company.html',args)


@login_required
def view_profile(request,pk=None):
    if pk:
        user=User.objects.get(pk=pk)
    else:
        user=request.user
    args={'user':user}
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

@login_required
def create_team(request):        #change password view
    if request.method=='POST':
        form=regteam(request.POST)
        if form.is_valid():
            form_instance=form.save(commit=False)
            form_instance.company_name=request.user.userprofile.company_name
            form_instance.save()
            return HttpResponse("successfully created a group")
        else:
            return redirect('/accounts/change-password')

    else:
        form=PasswordChangeForm(user=request.user)

        args={'form':form}
        return render(request,'accounts/change_password.html',args)
