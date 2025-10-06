from django.urls import path
from . import views

urlpatterns = [
    path('',views.contact_list,name='home'),
    path('register/',views.user_register,name='register'),
    path('add_contact/',views.add_contact,name='addcontact'),
    path('edit_contact/<int:id>',views.edit_contact,name='edit'),
    path('delete_contact/',views.delete_contact,name='delete'),
]
