from django.shortcuts import redirect, render
from .forms import UserRegistrationForm




# Create your views here.
def user_register(request):
    if request.method == 'POST':
        form_data = UserRegistrationForm(request.POST)
        if form_data.is_valid:
            form_data.save()
            return redirect ('login')
    else:
        form_data = UserRegistrationForm()
    return render(request,'register.html',{"forms":form_data})