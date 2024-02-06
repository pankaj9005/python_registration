from django.shortcuts import render
from django.shortcuts import redirect
from .models import User
# Create your views here.

def home(request):
    std=User.objects.all()
    return render(request,'std/home.html',{'std':std})

def std_add(request):
    if request.method=='POST':
        print('Added')
        #retreive the user inputs
        stds_name=request.POST.get('std_name')
        stds_mobile_number=request.POST.get('std_mobile_number')
        stds_email=request.POST.get('std_email')
        stds_age=request.POST.get('std_age')
        stds_gender=request.POST.get('std_gender')

        #create an object for models
        s=User()
        s.name=stds_name
        s.mobile_number=stds_mobile_number
        s.email=stds_email
        s.age=stds_age
        s.gender=stds_gender


        s.save()


    return render(request,'std/add_std.html',{})

def delete_std(request,age):
    s=User.objects.get(pk=age)
    s.delete()

    return redirect('/std/home')

def update_std(request,age):
    std=User.objects.get(pk=age)

    return render(request,'std/update_std.html',{'std':std})

def do_update_std(request,age):
    std_name=request.POST.get('std_name')
    std_mobile_number = request.POST.get('std_mobile_number')
    std_email = request.POST.get('std_email')
    std_age = request.POST.get('std_age')
    std_gender = request.POST.get('std_gender')

    std=User.objects.get(pk=age)

    std.name=std_name
    std.mobile_number = std_mobile_number
    std.email = std_email
    std.age = std_age
    std.gender = std_gender

    std.save()

    return redirect('/std/home')


def view_std(request,age):
    std = User.objects.get(pk=age)
    return render(request, 'std/view_std.html', {'std': std})

