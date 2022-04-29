from unicodedata import name
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect

from.models import User

from .forms import studentRegistration

# Create your views here.

#this function will add new item and show all items

def add_show(request):
    if request.method =='POST':
        fm= studentRegistration(request.POST) #here data sanga aaunxa 
        if fm.is_valid():
            nm= fm.cleaned_data['name']
            em= fm.cleaned_data['email']
            pw= fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save()
            fm= studentRegistration() #here without data or blank aaunxa 
            

    else:
        fm= studentRegistration()
    stud= User.objects.all()


    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud })

#this function will update or edit
def update_data(request,id):
    if request.method=='POST':
        pi = User.objects.get(pk=id)
        fm= studentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            
    else:
        pi = User.objects.get(pk=id)
        fm= studentRegistration(instance=pi)
    return render(request,'enroll/update.html',{'form':fm})


#this function will delete
def delete_data(request,id):
    if request.method=='POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

