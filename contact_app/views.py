from django.shortcuts import redirect, render, get_object_or_404
from .forms import UserRegistrationForm
from .models import Contact
from django.contrib.auth.decorators import login_required 




# Create your views here.
def user_register(request):
    if request.method == 'POST':
        form_data = UserRegistrationForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect ('register')
    else:
        form_data = UserRegistrationForm()
    return render(request,'register.html',{"forms":form_data})

# @login_required 
def add_contact(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        email = request.POST['email']
        phone_num = request.POST['phonenum']
        if fname and phone_num:
            Contact.objects.create(
                firstname = fname,
                email = email,
                phonenumber = phone_num
            )
            return redirect('home')
    return render(request,'add_contact.html')

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request,'contact_home.html',{'contacts': contacts})

def edit_contact(request,contact_id):
    contact = get_object_or_404(Contact,id=contact_id)

    if request.method == "POST":
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        phone_num = request.POST.get('phonenum')
        status = request.POST.get('status')
        if fname and phone_num:
            contact.firstname = fname
            contact.email = email
            contact.phonenumber = phone_num
            # contact.action = "status" in request.POST 
            contact.save()
            return redirect('home')
    return render(request,'edit.html',{'contacts':contact})




def delete_contact(request):
    return











# def complete_task(request,task_id):
#     task = get_object_or_404(Todo,id=task_id)
#     task.complete_task = True
#     task.save()
#     return redirect('home')

# def update_task(request,task_id):
#     task = get_object_or_404(Todo,id=task_id)

#     if request.method == "POST":
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         due_date = request.POST.get('due_date')
#         status = request.POST.get('status')
#         today = date.today()
#         if due_date and date.fromisoformat(due_date) < date.today():
#             return render(request, 'update_task.html', {
#                 'error': 'Due date cannot be in the past',
#                 'today': today
#             })
#         if title and description:
#             task.title =title
#             task.description = description
#             task.due_date = due_date if due_date else None
#             task.complete_task = "status" in request.POST 
#             task.save()
#             return redirect('home')
#     return render(request,'update_task.html',{'task':task})

# def delete_task(request,task_id):
#     task = get_object_or_404(Todo,id=task_id)
#     task.delete()
#     return redirect('home')