from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,AbstractUser
from django.contrib.auth import authenticate
import csv,io
from django.http import HttpResponse



from django.contrib import messages

def empl(request):
    if request.method== "POST":
        if request.POST.get('username') and request.POST.get('email') and request.POST.get('firstname') and request.POST.get('lastname'):
            username=request.POST['username']
            email=request.POST['email']
            first_name=request.POST['firstname']
            last_name=request.POST['lastname']
            password = request.POST['password']
            saveobj=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name)
            
            saveobj.set_password(password)

            saveobj.save()
            messages.success(request,"Register Successfully....")
            return redirect("empl")
        else:
            messages.info(request,"Some Field is Empty....")
            return redirect("empl")
    else:
        displayrecords=User.objects.all()
        return render(request,'index.html')

def delete1(request,id):
    var1=User.objects.get(id=id)
    var1.delete()
    return redirect("empl")

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        print(user)
        if user:
            print("LOGIN")
            return redirect('userlist')
        else:
            print("ERROR")
    else:        
        return render(request,'login.html')

def userlist(request):
    mydata = User.objects.all()
    return render(request,'userlist.html',{"employee":mydata})

def export_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="file.csv"'
    fieldnames = [ 'username','Email', 'First Name', 'Last Name']
    writer = csv.DictWriter(response, fieldnames=fieldnames)
    writer.writeheader()
    # User = get_user_model()
    all_users = User.objects.all()
    for user in all_users:
        writer.writerow({'username':user.username,
                         'Email': user.email,
                         'First Name': user.first_name,
                         'Last Name': user.last_name})

    return response   

# @login_required
def import_csv(request):
    csv_file = request.FILES.get('csv_file')
    try:
        if csv_file is not None:
            # User = get_user_model()
            
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file)
            next(reader)
            for i in reader:
                user=User(
                username=i[0],
                email = i[1],
                first_name = i[2],
                last_name = i[3]
                )
                user.save()
            messages.success(request,"Data ImportSuccessfully.........!!")     
            return redirect('userlist')
    except:
        return HttpResponse("Data Is alredy exits in this model....")
    return render(request,'import_csv.html')




