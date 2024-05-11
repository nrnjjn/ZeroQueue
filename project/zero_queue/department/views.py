from django.shortcuts import render
from department.models import Department

# Create your views here.
def department(request):
    if request.method=="POST":
        ob = Department()
        ob.department = request.POST.get('dept')
        ob.details = request.POST.get('details')
        ob.o_id = '1'
        ob.save()
    return render(request,'department/add_dept.html')

def search_dept(request):
    if request.method == "POST":
        vv=request.POST.get('department')
        obj = Department.objects.filter(department__icontains=vv)
        context = {
        'ok': obj
        }
        return render(request,'department/search department.html',context)
    return render(request,'department/search department.html')










