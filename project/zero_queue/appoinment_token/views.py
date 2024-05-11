from django.shortcuts import render

# Create your views here.


def token(request):
    return render(request,'appoinment_token/token.html')