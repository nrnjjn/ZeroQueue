from django.shortcuts import render
from working_hours.models import WorkingHours
import datetime

# Create your views here.

def view_hours(request):
    obj = WorkingHours.objects.all()
    context = {
        'objval': obj,
    }
    return render(request,'working_hours/update_working hours.html',context)
def hours(request):
    if request.method == "POST":
        ob = WorkingHours()
        ob.department = request.POST.get('department')
        ob.start_time= request.POST.get('working hours')
        ob.end_time= request.POST.get('hours')
        ob.date = datetime.date.today()
        ob.save()
    return render(request,'working_hours/post working hours.html')


def update(request,idd):
    obj = WorkingHours.objects.get(w_id=idd)
    context = {
        'objval': obj,
    }
    if request.method == "POST":
        ob = WorkingHours.objects.get(w_id=idd)
        ob.department = request.POST.get('department')
        ob.start_time= request.POST.get('working hours')
        ob.end_time= request.POST.get('hours')
        ob.date = datetime.date.today()
        ob.save()
        return view_hours(request)
    return render(request,'working_hours/update.html',context)
