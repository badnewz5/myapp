from django.urls import path
from . import views
from user.views import *


urlpatterns = [
    path('', views.home , name='index'), 
    path('user/', page_user , name='user'), 
    path('login', Pagelogin, name='login'), 
    path('logout', logoutuser,name='logout'), 
    path('register',register, name='register'),
    path('profile',profile_page, name='profile'),
    path('Experience',ExperienceForm, name='experience'),
    path('Edite_experience/<str:pk>/',edite_experience_page, name='edite_experience_page'),
    path('editskills/<str:pk>/',edit_skill_page, name='edit_skill_page'),
    path('delete_skill_page/<str:pk>/',delete_skill_page, name='delete_skill_page'),
    path('Skills',skill_page, name='skill_page'),
    path('Education',education_page, name='education_page'),
    path('Edit_Education/<str:pk>/',edit_education, name='edit_education'),
    path('blog',blog_page, name='blog_page'),
    path('editblog/<str:pk>/',edit_blog, name='edit_blog'),
    path('Personalinformation',Details_Personal, name='personal_information_page'),
]



