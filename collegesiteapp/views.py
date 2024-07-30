from django.shortcuts import render


def index(request):
    return render(request,'index.html')
def testpage(request):
    return render(request,'testpage.html')