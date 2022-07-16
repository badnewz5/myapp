from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import*



class FormRegistration(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserUpdate(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email']

class UpdateProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image']

class FormDetails(ModelForm):
    class Meta:
        model = Details
        fields = ['professional','address','email','firstname','middlename','lastname','phonenumber','experience_years','bio','gender']

class FormBlog(ModelForm):
    class Meta:
        model = Blog
        fields =['name','image','description']

class FormExperience(ModelForm):
    class Meta:
        model = Experience
        fields =['address','title','company_name','description','start_date','end_date','jobtype']

class FormSkill(ModelForm):
    class Meta:
        model = Skill
        fields =['name']

class FormEducation(ModelForm):
    class Meta:
        model = Education
        fields =['school_name','course_name','start_date','end_date']