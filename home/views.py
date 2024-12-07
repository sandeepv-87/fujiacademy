from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.
from django.shortcuts import render
import pdb
def my_home(request):
    data = {'key': 'value'}
    pdb.set_trace()  # Pause to inspect `request` or `data`
    return render(request, 'home.html', data)
def my_base(request):
    data = {'key': 'value'}
    pdb.set_trace()  # Pause to inspect `request` or `data`
    return render(request, 'base.html', data)
def my_contact(request):
    data = {'key': 'value'}
    pdb.set_trace()  # Pause to inspect `request` or `data`
    return render(request, 'contact.html', data)
def my_course(request):
    data = {'key': 'value'}
    pdb.set_trace()  # Pause to inspect `request` or `data`
    return render(request, 'courses.html', data)
def home(request):
    # return HttpResponse("this is my home page")
    return render(request, 'home.html')

def courses(request):
    # return HttpResponse("this is my website")
    return render(request, 'courses.html')

def aboutus(request):
    # return HttpResponse("this is my staff")
    return render(request, 'about.html')
def n3(request):
    return render(request,'n3.html')
def n4(request):
    return render(request,'n4.html')
def n5(request):
    return render(request,'n5.html')
def contact(request):
    # return HttpResponse("this is my about")
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST[
            'number']
        desc = request.POST['text']
        print(name,email,number,desc)
        lns = Contact(name=name,email=email,phone=number,desc=desc)
        lns.save()
        print("ok")
    return render(request, "contact.html")
