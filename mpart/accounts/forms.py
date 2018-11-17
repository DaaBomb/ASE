from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.forms import User
from .models import UserProfile,Company,teamtable

class RegistrationForm(UserCreationForm):      #Our own custom RegistrationForm
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=(
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self,commit=True):
        user=super(RegistrationForm,self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']
        #user.company_name=self.cleaned_data['company_name']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):  #our own custom edit profile form
    class Meta:
        model=User
        fields=(
            'email',
            'first_name',
            'last_name',
            'password',
        )
class ChangeProfileForm(forms.ModelForm):  #our own custom edit profile form
    class Meta:
        model=UserProfile
        fields=(
            'phone',
            'city',
        )

class customreg(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=(
            'Jobtitle',
            'city',
            'phone',
            'company_name',
        )

class customregcompany(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=(
            'Jobtitle',
            'city',
            'phone',
        )

class regcompany(forms.ModelForm):
    class Meta:
        model=Company
        fields=(
            'company_name',
        )
class regteam(forms.ModelForm):

    class Meta:
        model=teamtable
        fields=(
            'group_name',
        )
