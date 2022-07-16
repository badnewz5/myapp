from django.db import models
from django.utils import timezone
from django.shortcuts import render,reverse
from django.contrib.auth.models import User


class Profile(models.Model):
    image= models.ImageField(default='default.jpg', upload_to='profile',null=True,blank=True)
    user = models.OneToOneField(User , on_delete=models.CASCADE , null=True,blank=True)
    def __str__(self):
        return f'{self.user.username} Profile'



class Blog(models.Model):
    name = models.CharField(max_length=100 ,null=True)
    image= models.ImageField(default='default.jpg', upload_to='blog',null=True,blank=True)
    description= models.TextField(max_length=500,null=True,blank=True)
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True)
    def __str__(self):
        return self.name

class Experience(models.Model):
    STATUS = (
        ('Internship','Internship'),
        ('Parttime','Parttime'),
        ('Freelance','Freelance'),
        ('Fulltime','Fulltime'),
        ('Contracted','Contracted'),
        )
    title = models.CharField(max_length=100 ,null=True)
    company_name = models.CharField(max_length=100 ,null=True)
    address  = models.CharField(max_length=100 ,null=True)
    description= models.TextField(max_length=500,null=True,blank=True)
    achievement= models.TextField(max_length=100,null=True,blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now , null="True",blank="True")
    jobtype= models.CharField(max_length=100 ,null=True, choices=STATUS)
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True)
    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100 ,null=True)
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True)
    def __str__(self):
        return self.name

class Education(models.Model):
    school_name = models.CharField(max_length=100 ,null=True)
    course_name = models.CharField(max_length=100 ,null=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now , null="True",blank="True")
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True)
    def __str__(self):
        return self.school_name

class Details(models.Model):
    STATUS = (
        ('Male','Male'),
        ('Female','Female'),
        )
    professional = models.CharField(max_length=100 ,null=True,blank=True)
    firstname = models.CharField(max_length=100 ,null=True,blank=True)
    middlename = models.CharField(max_length=100 ,null=True,blank=True)
    lastname = models.CharField(max_length=100 ,null=True,blank=True)
    email = models.EmailField(max_length=100 ,null=True,blank=True)
    address = models.CharField(max_length=100 ,null=True,blank=True)
    phonenumber = models.CharField(max_length=100 ,null=True,blank=True)
    experience_years = models.CharField(max_length=100 ,null=True,blank=True)
    nationality = models.CharField(max_length=100 ,null=True,blank=True)
    birth = models.DateTimeField(default=timezone.now)
    bio = models.TextField(max_length=500,null=True,blank=True)
    gender= models.CharField(max_length=100 ,null=True, choices=STATUS)
    user = models.OneToOneField(User , on_delete=models.CASCADE , null=True,blank=True)
    def __str__(self):
        return self.professional;


    
