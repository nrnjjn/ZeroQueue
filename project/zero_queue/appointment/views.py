from django.shortcuts import render
from appointment.models import Appointment
# Create your views here.
def appo(request):
    obj = Appointment.objects.all()
    context = {
        'objval': obj,
    }
    return render(request,'appointment/appoinment.html',context)
def reject(request,idd):
    obj=Appointment.objects.get(a_id=idd)
    obj.status='reject'
    obj.save()
    return appo(request)
def aprv(request,idd):
    obj=Appointment.objects.get(a_id=idd)
    obj.status='aproved'
    obj.save()
    return appo(request)

def cancel(request):
    obj = Appointment.objects.all()
    context = {
        'objval': obj,
    }
    return render(request,'appointment/appointment cancel.html',context)
def cncl(request,idd):
    obj=Appointment.objects.get(a_id=idd)
    obj.status='canceled'
    obj.save()
    return cancel(request)


def view(request):
    obj = Appointment.objects.all()
    context = {
        'objval': obj,
    }
    return render(request,'appointment/view_appointment.html',context)

def status(request):
    obj =Appointment .objects.all()
    context = {
        'objval': obj,
    }
    return  render(request,'appointment/view_appointment status.html',context)
