from django.shortcuts import render
# Create your views here.
from app.forms import *
from app.models import *
from django.http.response import HttpResponse,HttpResponseRedirect

# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from time import time
def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        return render(request,'home.html',context={'username':username})
    return render(request,'home.html')

def userregister(request):
    UF=UserForm()
    d={'form':UF}
    if request.method=='POST':
        FD=UserForm(request.POST)
        if FD.is_valid():
            us=FD.save(commit=False)
            pw=FD.cleaned_data['password']
            us.set_password(pw)
            us.save()
            return HttpResponse('registered successfully')

    return render(request,'userregister.html',d)

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user and user.is_active:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('user is a not active user')
      
    return render(request,'user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def prime_for_else(request):
    t1=time()
    #a=int(input('enter a value'))
    a=1
    #b=int(input('enter b value'))
    b=1000
    L=[]
    for n in range(a,b):
        if n>1:
            for i in range(2,n//2+1):
                if n%i==0:
                    break
            else:
                L.append(n)
    t2=time()
    tk=t2-t1
    alg='prime_with_for_else'
    nop=len(L)
    un=request.session.get('username')
    UO=User.objects.get(username=un)
    po=Profile.objects.get_or_create(user=UO,time=str(t1),LL=a,UL=b,timetaken=tk,algorithm=alg,no_of_primes=nop)[0]
    po.save()
    return HttpResponse(po.algorithm)


    












