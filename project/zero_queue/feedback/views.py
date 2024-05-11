from django.shortcuts import render
from feedback.models import Feedback
import datetime


# Create your views here.
def feedback(request):
    if request.method=="POST":
        ob = Feedback()
        ob.feedback = request.POST.get('feedback')
        ob.date = datetime.date.today()
        ob.time = datetime.datetime.now()
        ob.u_id = '1'
        ob.save()
    return render(request,'feedback/feedback.html')

def view(request):
    obj = Feedback.objects.all()
    context = {
        'objval': obj,
    }
    return render(request,'feedback/view_feedback.html',context)




