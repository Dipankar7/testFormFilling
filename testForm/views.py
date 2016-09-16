from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request,'home.html',{})

@login_required
def success(request):
    return render(request,'success.html',{})
@login_required
def copypaste(request):
    print request.GET
    if request.method=="POST":
        print "came here"
        print request.POST
    return render(request,'copypaste.html',{})
