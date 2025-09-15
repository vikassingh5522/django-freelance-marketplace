from django.shortcuts import render ,redirect
from django.http import HttpResponse
from application.models import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from .serializers import enquiry_tableSerializer
from rest_framework.response import Response
from datetime import datetime
from rest_framework.views import APIView

# Create your views here.

def home(request):
     return render(request, 'index.html')


def about(request):
     return render(request, 'about.html')

def services(request):
     return render(request, 'services.html')

def project(request):
     return render(request, 'project.html')

def happiness(request):
     return render(request, 'happiness.html')

def contact(request):
     
     if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('phone')
        d = request.POST.get('subject')
        e = request.POST.get('message')
        enquiry = enquiry_table(name = a, email = b, phone = c, subject = d, message = d)
        enquiry.save()
        
        messages.success(request,'Enquiry Form Submitted Successfully...')
        
     return render(request, 'contact.html')




def login_user(request):
     
          if request.method == 'POST':
            a = request.POST.get('username')
            b = request.POST.get('password')

            user = authenticate(request, username = a, password = b)
        
            if user is not None:
              login(request, user)
            
            return redirect('Dashboard')
            
          else:
            
           messages.error(request, 'In-correct username or password!..')
          
          # user = None                       
          # if request.method == 'POST':
          #  a = request.POST['username' , '']           #enquiry_table
          #  b = request.POST['password' , '']
           
          #  user = authenticate(request, username=a, password=b)

          # if user is not None:
          #    login(request, user)
          #    request.session['username_id'] = a 
          #    return redirect('Dashboard')
          # else:
          #   messages.error(request, 'Incorrect username or password!..')
           
          return render(request, 'login.html')
   
@login_required(login_url='login')

def dashboard(request):
    print("Hi, The user name is: ",request.session.get('username_id'))

    return render(request, 'dashboard/index.html')

@login_required(login_url='login')
   
def dashboard(request):
          
    return render(request, 'dashboard/index.html')


def enquiry_details(request):

    info = enquiry_table.objects.all()

    records = { 'abc':info }

    return render(request, 'dashboard/tables.html', records)
   
def delete_record(request, id):
     
    if request.method=='POST':
        data = enquiry_table.objects.get(pk=id)
        data.delete()
    return HttpResponseRedirect('/enquiry_details/')

def edit_record(request, id):
    info = enquiry_table.objects.filter(pk=id)
    
    data = {'information':info}
    return render(request, 'dashboard/editrecord.html', data)


def update_record(request, id):
    info = enquiry_table.objects.get(pk=id)
    
    info.name = request.POST.get('name')
    info.email = request.POST.get('email')
    info.phone = request.POST.get('phone')
    info.message = request.POST.get('message')
    info.date_field = request.POST.get('date')
    info.save()
    
    return HttpResponseRedirect('/enquiry_details/')

 
def logout_user(request):
    logout(request)
    return redirect('/')
   

def reports(request):

    data = None

    if request.method =='POST':
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        
        fromdate = datetime.strptime(fromdate, '%Y-%m-%d').date()
        todate   = datetime.strptime(todate, '%Y-%m-%d').date()
        
        
        searchresult = enquiry_table.objects.filter(date_field__range=[fromdate, todate])

        data = {"information":searchresult}


    return render(request, 'dashboard/reports.html', data)
   
   
class student_data(APIView):
    def get(self, request, format=None):
        data = enquiry_table.objects.all()
        serializer = enquiry_tableSerializer(data, many=True)
        return Response(serializer.data)
