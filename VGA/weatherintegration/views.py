from django.shortcuts import render

# Create your views here.
def weatherintegration(request):
    return render(request,'userapp/weatherintegration.html')