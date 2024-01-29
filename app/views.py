from django.shortcuts import render
from .models import SignupData, QueryData
from django.db.models import Q
# Create your views here.


def home(request):
    return render(request,'app/home.html')

def Signup(request):
    return render(request,'app/Signup.html')

def Login(request):
    return render(request,'app/Login.html')

def about(request):
    return render(request,'app/about.html')

def Contact(request):
    return render(request,'app/Contact.html')
      
def Services(request):
    return render(request,'app/Services.html')

def savedata(request):
    if request.method=='POST':
        name=request.POST['Name']
        email=request.POST['email']
        contact=request.POST['number']
        pswd=request.POST['password']
        cpswd=request.POST['cpassword']

        user=SignupData.objects.filter(Email=email)
        if user:
            msg = "User already exist"
            return render(request,'app/Signup.html',{'msg':msg})
        else:
            if pswd==cpswd:
                newuser=SignupData.objects.create(Name=name,
                                                Email=email,
                                                Contact=contact,
                                                Password=pswd,
                                                confPassword=cpswd )
                
                message = "User register Successfully"
                return render(request,"app/Login.html",{'msg1':message})
        
            else:
                message = "Password and Confirm Password Does not Match"
                return render(request,"app/Signup.html",{'incoreectmsg':message})
    else:
        return render(request,'app/Signup.html')

def Login_data(request):
    if request.method=='POST':
        email=request.POST['email']
        log_pswd=request.POST['password']
       
        data=SignupData.objects.get(Email=email)
        # print(data)
        if data:
            if email==data.Email and log_pswd==data.Password:     
                name=data.Name
                email=data.Email
                contact=data.Contact
                password=data.Password
                cpasword=data.confPassword
                
                user={
                    'Name':name,
                    'Email':email,
                    'Contact':contact,
                    'Password':password,
                    'CnfPassword':cpasword,
                    }
                return render(request,'app/dashboard.html',user)
         
            else:
                message ="Incorrect password or E-mail"
                return render(request,"app/Login.html",{'incoreectmsg':message})
    else:
        return render(request,'app/Login.html')


def query(request):
    if request.method=='POST':
        qry_email=request.POST['email']
        qry_name=request.POST['Query']

        QueryData.objects.create(Query=qry_name,
                                 QueryEmail=qry_email)

        data = SignupData.objects.get(Email=qry_email)
        name=data.Name
        email=data.Email
        contact=data.Contact
        password=data.Password
        cpasword=data.confPassword
        
        user={
            'Name':name,
            'Email':email,
            'Contact':contact,
            'Password':password,
            'CnfPassword':cpasword
            }

        return render(request,'app/dashboard.html',user)
       
def ShowData(request,pk):
    Qdata=QueryData.objects.filter(QueryEmail=pk)

    data=SignupData.objects.get(Email=pk)
    name=data.Name
    email=data.Email
    contact=data.Contact
    password=data.Password
    cpasword=data.confPassword

    user={
        'Name':name,
        'Email':email,
        'Contact':contact,
        'Password':password,
        'CnfPassword':cpasword,
    }

    return render(request,'app/table.html',{'key1':Qdata,'user':user})

def edit(request,editId):
    Qdata=QueryData.objects.get(id=editId)
    email=Qdata.QueryEmail

    Signdata=SignupData.objects.get(Email=email)
    name=Signdata.Name
    email=Signdata.Email
    contact=Signdata.Contact
    password=Signdata.Password
    cpasword=Signdata.confPassword

    user={'name':name,
          'Email':email,
          'Contact':contact,
          'Password':password,
          'Conpass':cpasword
        }

    all_data=QueryData.objects.filter(QueryEmail=email)

    return render(request,'app/Update.html',{'edi':Qdata,'key':all_data,'user':user})

def delete(request,delId):
    Qdata=QueryData.objects.get(id=delId)
    email=Qdata.QueryEmail

    Qdata.delete()
    data=SignupData.objects.get(Email=email)
    name=data.Name
    email=data.Email
    contact=data.Contact
    password=data.Password
    cpasword=data.confPassword

    user={
        'Name':name,
        'Email':email,
        'Contact':contact,
        'Password':password,
        'CnfPassword':cpasword,
    }
    all_data=QueryData.objects.filter(QueryEmail=email)
    return render(request,'app/table.html',{'key1':all_data,'user':user})

def Update(request,upId):
    Updata=QueryData.objects.get(id=upId)   
    Updata.QueryEmail=request.POST['UpdataEmail']
    Updata.Query=request.POST['UpdataQuery']

    Updata.save()  #update query

    Signdata=SignupData.objects.get(Email=Updata.QueryEmail)
    name=Signdata.Name
    email=Signdata.Email
    contact=Signdata.Contact
    password=Signdata.Password
    cpasword=Signdata.confPassword

    user={'name':name,
          'Email':email,
          'Contact':contact,
          'Password':password,
          'Conpass':cpasword,
    }
    all_data=QueryData.objects.filter(QueryEmail=Updata.QueryEmail)

    return render(request,'app/table.html',{'key1':all_data,'user':user})

def search(request,pk):    
    SQuery=request.POST['search']
    
    data=SignupData.objects.get(Email=pk)
    name=data.Name
    email=data.Email
    contact=data.Contact
    password=data.Password
    cpasword=data.confPassword

    user={
        'Name':name,
        'Email':email,
        'Contact':contact,
        'Password':password,
        'CnfPassword':cpasword,
    }

    data=QueryData.objects.filter(Q(QueryEmail=email) & Q(Query=SQuery))
    return render(request,'app/table.html',{'key1':data,'user':user})

def back(request,pk):
    data=SignupData.objects.get(Email=pk)
    name=data.Name
    email=data.Email
    contact=data.Contact
    password=data.Password
    cpasword=data.confPassword
    user={
        'Name':name,
        'Email':email,
        'Contact':contact,
        'Password':password,
        'CnfPassword':cpasword,
        }
    return render(request,'app/dashboard.html',user)
    

    














    