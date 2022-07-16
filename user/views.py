from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate,login , logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from . models import*
from . forms import*
from . forms import FormDetails

# Create your views here.

@login_required(login_url='login')
def page_user(request):
    skills = Education.objects.all()
    alls = Skill.objects.all()
    posts = Experience.objects.all()
    blogs = Blog.objects.all()
    context = {'skills':skills,'alls':alls,'posts':posts,'blogs':blogs}
    return render(request , 'User/user.html',context)

def Pagelogin(request):

    if request.user.is_authenticated:
        return redirect('user')
    else:
        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request , username=username , password=password)

            if user is not None:
                login(request, user)
                return redirect('user')
            else:
                messages.info(request , 'Username or Password is incorrect try again')
    return render(request , 'auth/login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('user')
    else:
        form = FormRegistration()
        if request.method == 'POST':
            form = FormRegistration(request.POST)
            username = request.POST.get('username')
            email = request.POST.get('email')
            pass1 = request.POST.get('password1')
            pass2 = request.POST.get('password2')
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created' + username)
            
            return redirect('login')

            
    context = {'form':form}
    return render(request , 'auth/register.html',context)

def logoutuser(request):
    logout(request)
    return redirect('index')
    
@login_required(login_url='login')
def profile_page(request):
    skills = Education.objects.all()
    alls = Skill.objects.all()
    posts = Experience.objects.all()
    details = Details.objects.all()
    if request.method == 'POST':
        form1 = UserUpdate(request.POST, instance=request.user)
        form2 = UpdateProfileForm(request.POST, request.FILES , instance=request.user.profile)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            messages.success(request, f'Your Account has been Updated!')
            return redirect('profile')
    else:
        form1 = UserUpdate(instance=request.user)
        form2 = UpdateProfileForm(instance=request.user.profile)


       

    context = {'details':details, 'form1':form1 , 'form2':form2,'skills':skills,'alls':alls,'posts':posts}
    return render(request, 'setting/profile.html',context);

@login_required(login_url='login')
def page_personal(request):
    form = FormBlog()
   
    return render(request,'setting/personal_information.html',{'form':form});


@login_required(login_url='login')
def ExperienceForm(request):
    form = FormExperience()
    posts = Experience.objects.all()
    skills = Education.objects.all()
    alls = Skill.objects.all()
    if request.method == 'POST':
        form = FormExperience(request.POST)
        name=request.POST.get('address')
        description=request.POST.get('description')
        company_name=request.POST.get('company_name')
        start_date=request.POST.get('start_date')
        end_date=request.POST.get('end_date')
        jobtype=request.POST.get('jobtype')
        title=request.POST.get('title')
        if form.is_valid():
            form.save()
            messages.success(request, 'Completed add experience!')
            return redirect('experience')
    context = {'form':form,'alls':alls,'alls':alls,'posts':posts,'skills':skills}
    return render(request,'Experience/experience.html',context);

@login_required(login_url='login')
def edite_experience_page(request,pk):
    posts = Experience.objects.get(id=pk)
    skills = Education.objects.all()
    alls = Skill.objects.all()
    form = FormExperience(instance=posts)
    if request.method == 'POST':
        form = FormExperience(request.POST,instance=posts)
        name=request.POST.get('address')
        description=request.POST.get('description')
        company_name=request.POST.get('company_name')
        start_date=request.POST.get('start_date')
        end_date=request.POST.get('end_date')
        jobtype=request.POST.get('jobtype')
        title=request.POST.get('title')
        if form.is_valid():
            form.save()
            messages.success(request, 'Completed update experience!')
            return redirect('experience')
    context = {'form':form,'alls':alls,'alls':alls,'posts':posts,'skills':skills}
    return render(request,'Experience/editexperience.html',context);

@login_required(login_url='login')
def skill_page(request):
    form = FormSkill()
    skills = Education.objects.all()
    alls = Skill.objects.all()
    posts = Experience.objects.all()
    if request.method =='POST':
        form = FormSkill(request.POST)
        name=request.POST.get('name')
        if form.is_valid():
            form.save()
            messages.success(request, 'Completed add skills !')
            return redirect('skill_page')
    context = {'form':form,'alls':alls,'alls':alls,'posts':posts,'skills':skills}

    return render(request, 'Skills/skill.html',context)

@login_required(login_url='login')
def edit_skill_page(request,pk):
    skills = Education.objects.all()
    alls = Skill.objects.all()
    jobs=Skill.objects.get(id=pk)
    posts = Experience.objects.all()
    form = FormSkill(instance=jobs)
    if request.method =='POST':
        form = FormSkill(request.POST , instance=jobs)
        name=request.POST.get('name')
        if form.is_valid():
            form.save()
            messages.success(request, 'Completed update your skills!')
            return redirect('skill_page')
    context = {'jobs':jobs,'form':form,'alls':alls,'alls':alls,'posts':posts,'skills':skills}

    return render(request, 'Skills/editskill.html',context)

@login_required(login_url='login')
def delete_skill_page(request,pk):
    details=Skill.objects.get(id=pk)
    if request.method == 'POST':
        details.delete()
        return redirect('skill_page')
    context ={'details':details}

    return render(request, 'Skills/skill.html',context)

@login_required(login_url='login')
def education_page(request):
    form =FormEducation()
    skills = Education.objects.all()
    alls = Skill.objects.all()
    if request.method =='POST':
        form = FormEducation(request.POST)
        name=request.POST.get('school_name')
        name2=request.POST.get('course_name')
        name3=request.POST.get('start_date')
        name4=request.POST.get('end_date')
        if form.is_valid():
            form.save()
            messages.success(request, 'Completed add education !')
            return redirect('education_page')
    context = {'form':form,'alls':alls,'skills':skills}



    return render(request, 'Education/education.html',context)

@login_required(login_url='login')
def edit_education(request,pk):
    skills = Education.objects.all()
    pages = Education.objects.get(id=pk)
    alls = Skill.objects.all()
    form =FormEducation(instance=pages)
    if request.method =='POST':
        form = FormEducation(request.POST,instance=pages)
        name=request.POST.get('school_name')
        name2=request.POST.get('course_name')
        name3=request.POST.get('start_date')
        name4=request.POST.get('end_date')
        if form.is_valid():
            form.save()
            messages.success(request, 'Completed update education !')
            return redirect('education_page')
    context = {'form':form,'alls':alls,'skills':skills,'pages':pages}



    return render(request, 'Education/editeducation.html',context)

@login_required(login_url='login')
def blog_page(request):
    blogs = Blog.objects.all()
    skills = Education.objects.all()
    alls = Skill.objects.all()
    form = FormBlog()
    if request.method == 'POST':
        form = FormBlog(request.POST , request.FILES)
        name=request.POST.get('name')
        description=request.POST.get('description')
        image=request.POST.get('image')
        if form.is_valid():
            form.save()
            messages.success(request, 'Completed add blog!')
            return redirect('blog_page')
    context = {'blogs':blogs,'form':form,'alls':alls,'skills':skills}
    return render(request,'blog/blog.html',context);

@login_required(login_url='login')
def edit_blog(request,pk):
    blogs = Blog.objects.get(id=pk)
    skills = Education.objects.all()
    alls = Skill.objects.all()
    form = FormBlog(instance=blogs)
    if request.method == 'POST':
        form = FormBlog(request.POST , request.FILES, instance=blogs)
        name=request.POST.get('name')
        description=request.POST.get('description')
        image=request.POST.get('image')
        if form.is_valid():
            form.save()
            messages.success(request, 'Completed update blog!')
            return redirect('blog_page')
    context = {'blogs':blogs,'form':form,'alls':alls,'skills':skills}
    return render(request,'blog/edit_blog.html',context);

@login_required(login_url='login')
def Details_Personal(request):
    form = FormDetails()
    skills = Education.objects.all()
    alls = Skill.objects.all()
    details = Details.objects.all()
    if request.method == 'POST':
        form = FormDetails(request.POST)
        professional = request.POST.get('professional')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        middlename = request.POST.get('middlename')
        gender = request.POST.get('gender')
        phonenumber = request.POST.get('phonenumber')
        address = request.POST.get('address')
        bio = request.POST.get('bio')
        experience_years = request.POST.get('experience_years')
        email = request.POST.get('email')
        if form.is_valid():
            form.save()
            messages.success(request, 'Completed add personal information!')
            return redirect('personal_information_page')
    
    context = {'form':form,'alls':alls,'skills':skills,'details':details}

    return render(request, 'Personalinformation/personal_information.html',context)