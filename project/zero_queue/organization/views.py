from django.shortcuts import render
from organization.models import ManageOrganization
from  login.models import Login

# Create your views here.
def register(request):
    if request.method=="POST":
        ob = ManageOrganization()
        ob.name = request.POST.get('name')
        ob.address = request.POST.get('address')
        ob.phone_no = request.POST.get('number')
        ob.email = request.POST.get('email')
        ob.working_hours=request.POST.get('wrk')
        ob.status="pending"
        ob.save()
    return render(request, 'organisation/register.html')
def organisation(request):
    obj=ManageOrganization.objects.all()
    context={
        'objval':obj
    }
    return render(request,'organisation/manage_organisation.html',context)
def aprove(request,idd):
    obj=ManageOrganization.objects.get(o_id=idd)
    obj.status='aprove'
    obj.save()
    ob=Login()
    ob.username=request.POST.get('email')
    ob.password=request.POST.get('name')
    ob.u_id=obj.o_id
    ob.save()
    return organisation(request)

def reject(request,idd):
    obj=ManageOrganization.objects.get(o_id=idd)
    obj.status='reject'
    obj.save()
    return organisation(request)


def org(request):
    if request.method == "POST":
        ob = ManageOrganization()
        ob.name = request.POST.get('organisation')
        ob.save()
    return render(request,'organisation/organisation.html')
def search(request):
    return render(request,'organisation/search organisation.html')




