from django.shortcuts import render
from  complaints.models import Complaints
import datetime
# Create your views here.
def complaints(request):
    obj=Complaints.objects.filter(reply='pending')
    context={
        'objval':obj

    }
    return render(request,'complaints/view_cmp.html',context)
def post(request,idd):
    ob=Complaints.objects.get( c_id=idd)
    if request.method=='POST':



        ob.reply = request.POST.get('reply')
       # ob.u_id = 1
       # ob.date = datetime.date.today()
       # ob.time = datetime.datetime.now()
        ob.save()

        return complaints(request)

    return render(request,'complaints/post.html')


