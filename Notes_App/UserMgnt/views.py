from django.shortcuts import render
from botocore.vendored.requests.api import request
from django.template import response
from django.contrib.auth.decorators import login_required
import logging
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.hashers import make_password
from lib2to3.fixes.fix_input import context
from django.core.mail.message import EmailMultiAlternatives
from uuid import uuid4
import uuid
import smtplib
from Notes_App import settings
from cgitb import html
import socket
from django_ajax.decorators import ajax
from UserMgnt.models import notes


def login(request):
    
    context= dict()
    print("context")
    return render(request,'UserMgnt/login.html',context)

# function check login form
def dashboard(request):
    
    context= dict()
    try:
        
        uname = request.POST['username']
        pwd = request.POST['password']
        context['username']=uname
        
#         context['msg']="The username and password you entered don't match."
        
        try:
            user = User.objects.get(username=uname)
            if(user.check_password(pwd)):
        #         print("In If")
                return render(request,'UserMgnt/dashboard.html',context)
            else:
        #         print("In else")
                context['login_error']=1
                return render(request,'UserMgnt/login.html',context)
        except(User.DoesNotExist):
            print("in ex 1")
            context['msg']="Username and Password are required."
            return render(request,'UserMgnt/login.html',context)
    except MultiValueDictKeyError:
        print("in ex 2")
#         context['msg']="Both Username and Password are required."
        return render(request,'UserMgnt/login.html',context)
    
    
def new_acc(request):
    
    return render(request, 'UserMgnt/new_acc.html')


# function for creating new user for system
def acc_reg(request):
    
    context=dict()
    
    username = request.POST["new_user"]
    password = request.POST["new_pass"]
    email = request.POST["new_email"]
    try:
#         checking all required fields are entered or not
        print("in 1st try")    
        if username !="" and password !="" and email !="":
            try:
  
                user_obj = User.objects.all()
                print("user obj",user_obj)
                
#                if there is no user in system
                if not user_obj:
        
                    en_password=make_password(password, salt=None, hasher='pbkdf2_sha256')
                    newuser = User(username = username , password = en_password , email = email)
                    newuser.save()
                    print("user saved")
                    context['smsg']=username
                    context['flag']= 1
                    return render(request, 'UserMgnt/new_acc.html',context)
                
#                 creating users for system
                for i in user_obj:
                    print("in try",i.username)
                    if username != i.username and email != i.email:
                        print("In if")
                        en_password=make_password(password, salt=None, hasher='pbkdf2_sha256')
                        newuser = User(username = username , password = en_password , email = email)
                        newuser.save()
                        print("user saved")
                        context['smsg']=username
                        context['flag']= 1
                        return render(request, 'UserMgnt/new_acc.html',context)
                    
#                    if user is already exists in system
                    else:
                        context['msg']="User Already Exist"
                        print("in else")
                        return render(request, 'UserMgnt/new_acc.html',context)
            except:
                pass
            
#        if user did not fill all required fields
        else:
            context['msg']="Enter All Details"
            print("In 2 else ")    
            return render(request, 'UserMgnt/new_acc.html',context)

            
#        if user did not fill all required fields              
    except:
        context['msg']="Enter All Details"
        print("In except")    
        return render(request, 'UserMgnt/new_acc.html',context)
    
    
    
def index(request):
    
    context = dict()
    return render(request, 'UserMgnt/index.html',context)

def forgot_pass(request):
    
    return render(request, 'UserMgnt/forgot_pass.html')


# function, if user forgot password
def forgot_pass_change(request):
    
    context = dict()
    uname = request.GET['f_uname']
    uemail = request.GET['f_email']
    pass1 = request.GET['f_pass1']
    pass2 = request.GET['f_pass2']
    
    print("name-",uname)
    print("email-",uemail)
    password = User.objects.make_random_password()
    print("password is : "+password)
    
#     checking all required fields are entered or not
    if uname !="" and uemail !="" and pass1!="" and pass2!="":
        print("in if")
        try:
            user = User.objects.get(username=uname)
            print("user email",user.email)
            user_email = user.email
            if user_email == uemail:
                if pass1 == pass2:
                   
                   user.set_password(pass2)
                   user.save()
                   context['msg']="Password Has Beed Changed"
                   return render(request, 'UserMgnt/forgot_pass.html',context)
               
#                if both passwords are not match
                else:
                    context['msg']="Both Password Should Match"
                    return render(request, 'UserMgnt/forgot_pass.html',context)
                
#            if email address for your account does not matches     
            else:
                context['msg']="Invalid Email"
                return render(request, 'UserMgnt/forgot_pass.html',context)
            
#         if user does not exists in system
        except(User.DoesNotExist):
            context['msg']="User Does Not Exist"
            return render(request, 'UserMgnt/forgot_pass.html',context)
        
#    if user did not fill all required fields     
    else:
        print("in else")
        context['emsg']="Please Enter All details."
        return render(request, 'UserMgnt/forgot_pass.html',context)
    


# creating new note and saving it in notes table
@ajax
def save_note(request):
    
    n_name = request.GET['n_name']
    n_cnt = request.GET['n_cnt']
    crnt_user = request.GET['crnt_user']
    
    u = User.objects.get(username=crnt_user)
    uid=u.id
    note = notes(n_name=n_name,n_owner=crnt_user,n_content=n_cnt,owner_id_id=uid,mark_complete=0)
    note.save()
    print("note has been created")
        
    
    