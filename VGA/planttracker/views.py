from django.shortcuts import render

# Create your views here.
def planttracker(request):
    return render(request,'userapp/planttracker.html')