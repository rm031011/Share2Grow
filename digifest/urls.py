from django.contrib import admin
from django.urls import path
from digifest import views

urlpatterns = [
    path('', views.index,name='home'),
    path('vote/', views.citpage),
    path('pol_log/', views.log),
    path('civil/',views.problem),
    path('pol_log/signup.html/', views.signup),
    path('mainifest.html/', views.manifest),
    path('result.html/', views.result),
    path('mainifest.html/result.html/', views.result),
    path('pol_log/signup.html/register_user/', views.register),
    path('pol_log/hello/', views.logged),
    path('insert/', views.ins_rev),
    path('resu/', views.result),
    path('list/', views.list)

]
