from django.shortcuts import render

# Create your views here.
def gardenplanning(request):
    return render(request,'userapp/garden_planning.html')