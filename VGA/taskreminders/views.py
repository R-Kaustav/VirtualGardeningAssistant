from django.shortcuts import render

# Create your views here.
def taskreminder(request):
    return render(request,'userapp/taskreminder.html')