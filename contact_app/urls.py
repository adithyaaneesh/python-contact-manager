from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.contact_list, name='home'),
    path('', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_contact/', views.add_contact, name='addcontact'),
    path('edit_contact/<int:contact_id>/', views.edit_contact, name='edit'),
    path('delete_contact/<int:contact_id>/', views.delete_contact, name='delete'),
    path('userprofile/', views.user_profile, name='userprofile'),
    path('admindashboard/', views.admin_dashboard, name='admindashboard'),
]
