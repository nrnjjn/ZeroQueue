from django.shortcuts import render
from cancellation.models import Cancellation
from appointment.models import Appointment
# Create your views here.
def cancel(request):
    obj = Appointment.objects.filter(status='canceled')
    context = {
        'objval': obj,
    }

    return render(request,'cancellation/view_cancellation.html',context)

