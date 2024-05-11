from django.shortcuts import render
from register.models import Register

# Create your views here.



def user(request):
    if request.method=="POST":
        ob = Register()
        ob.name = request.POST.get('name')
        ob.date_of_birth = request.POST.get('date')
        ob.age = request.POST.get('age')
        ob.gender = request.POST.get('gender')
        ob.email = request.POST.get('email')
        ob.address = request.POST.get('address')
        ob.guardian = request.POST.get('guardian')
        ob.phone_number = request.POST.get('number')
        ob.password = request.POST.get('password')
        ob.save()


    return render(request,'register/user_register.html')

