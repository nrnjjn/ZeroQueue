from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'temp/index.html')
def admin(request):
    return  render(request,'temp/admin.html')
def organisation(request):
    return render(request,'temp/organisation.html')
def user(request):
    return  render(request,'temp/user.html')