from django.shortcuts import render
from facility.models import Facilities
# Create your views here.
def facility(request):
    if request.method=="POST":
     ob = Facilities()
     ob.facilities = request.POST.get('facilities')
     ob.details = request.POST.get('details')
     ob.o_id = '1'
     ob.save()
    return render(request,'facility/add_facilities.html')

def view(request):
    obj=Facilities.objects.all()
    context={
        'objval': obj,
    }
    return render(request,'facility/view_facilities.html',context)



