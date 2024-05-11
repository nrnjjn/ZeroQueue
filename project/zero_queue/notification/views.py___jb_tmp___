from django.shortcuts import render
from notification.models import Notification
import datetime

# Create your views here.

def notification(request):
    if request.method=="POST":
        ob = Notification()
        ob.notification = request.POST.get('notification')
        ob.date = datetime.date.today()
        ob.save()


    return render(request,'notification/notification.html')



def view(request):
    obj=Notification.objects.all()
    context={
        'objval':obj
    }

    return render(request,'notification/view_notification.html',context)

