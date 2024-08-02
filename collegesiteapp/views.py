from django.shortcuts import render


def index(request):
    return render(request,'index.html')
def testpage(request):
    return render(request,'testpage.html')

def keytonespeakers(request):
    return render(request,'keytonespeakers.html')

def registration(request):
    return render(request,'registration.html')

def callforpapers(request):
    return render(request,'callforpapers.html')

def submitpaper(request):
    return render(request,'submitpaper.html')

def publication(request):
    return render(request,'publication.html')

def venue(request):
    return render(request,'venue.html')