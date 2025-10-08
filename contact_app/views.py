from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .models import Contact
from django.contrib.auth.models import User 



def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})



def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  

            if user.is_superuser:
                return redirect('admindashboard')  
            return redirect('home')

        return render(request, "login.html", {'error': 'Invalid username or password'})

    return render(request, "login.html")


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')



@login_required
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user)
    return render(request, 'contact_home.html', {'contacts': contacts})


@login_required
def add_contact(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        phone_num = request.POST.get('phonenum')

        if fname and phone_num:
            Contact.objects.create(
                user=request.user,
                firstname=fname,
                email=email,
                phonenumber=phone_num,
            )
            return redirect('home')
    return render(request, 'add_contact.html')

@login_required
def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id,user=request.user)

    if request.method == "POST":
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        phone_num = request.POST.get('phonenum')

        if fname and phone_num:
            contact.firstname = fname
            contact.email = email
            contact.phonenumber = phone_num
            contact.save()
            return redirect('home')

    return render(request, 'edit.html', {'contact': contact})


@login_required
def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id,user=request.user)
    contact.delete()
    return redirect('home')


@login_required
def user_profile(request):
    user = request.user
    return render(request, 'user_profile.html',{'user':user})

@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('home') 
    user_only = User.objects.filter(is_superuser=False)
    users = User.objects.all()
    contacts = Contact.objects.all()

    context = {
        'user_only': user_only,
        'users': users,
        'contacts': contacts,
        'user_only_count':user_only.count(),
        'user_count': users.count(),
        'contact_count': contacts.count(),
    }
    return render(request, 'admin_dashboard.html', context)

@login_required
def admin_profile(request):
    return render(request,'admin_profile.html')

@login_required
def admin_contact(request):
    contacts = Contact.objects.filter(user__is_superuser=False)
    return render(request,'admin_contacts.html',{'contacts':contacts})

@login_required
def admin_users(request):
    contacts = Contact.objects.filter(user__is_superuser=False)
    # users = User.objects.all()
    # context = {
    #     'users':users
    # }
    return render(request,'admin_users.html',{'contacts':contacts})
