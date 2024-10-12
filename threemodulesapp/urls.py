from django.urls import path
from . import views

urlpatterns = [
    path('admin1/', views.admin1, name='admin1'),
    path('about/', views.about, name='about'),
    path('teacher/', views.teacher, name='teacher'),
    path('student/', views.student, name='student'),
    path('studentreg/', views.studentreg, name='studentreg'),
    path('teacherreg/', views.teacherreg, name='teacherreg'),
    path('doregister/', views.doregister, name='doregister'),
    path('pregisteration/', views.pregisteration, name='pregisteration'),
    path('login/', views.login1, name='login1'),
    path('', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
]