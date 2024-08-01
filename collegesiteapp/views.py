from django.shortcuts import render


def index(request):
    return render(request,'index.html')
def testpage(request):
    return render(request,'testpage.html')

def keytonespeakers(request):
    return render(request,'keytonespeakers.html')

def registration(request):
    return render(request,'registration.html')

def venue(request):
    return render(request,'venue.html')