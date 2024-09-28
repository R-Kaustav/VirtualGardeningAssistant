from django.shortcuts import render

# Create your views here.
def gardeningtips(request):
    return render(request,'userapp/gardening_tips.html')