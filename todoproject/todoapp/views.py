from django.shortcuts import render  , redirect
from .models import Task
from django.contrib.auth.models import User , auth
from django.contrib import messages

def home(request):
    return render(request ,'index.html')

def about_me(request):
    return render(request , 'about.html')

def add_task(request):
	if request.method=='POST':
		title = request.POST.get('tt')
		description = request.POST.get('dep')
		myimg = request.FILES.get('image')
		myvideo = request.FILES.get('video')
		print(myimg)
		data_op = Task(Title = title , Description =description , image = myimg , video = myvideo )
		data_op.save()
		return redirect("data")
	return render(request , 'post.html')

#get Data from the Database
def get_data(request):
    All_data = Task.objects.all()
    # fetching the data
     
    data = {
        'key' :All_data
    }
    return render(request , 'All_task.html' , data)

def edit_data(request , parm):
    if request.method == 'POST':
        title = request.POST.get('tt')
        description = request.POST.get('dep')
        update_data = Task(id = parm , Title = title , Description = description)
        update_data.save()
        return redirect('data')
    else:
        specific_data = Task.objects.all().filter(id = parm)
        data = {
        'key' :specific_data
        }
    return render(request , 'edit.html' , data)

def delete_data(request , p):
    sepecific_data = Task.objects.all().filter(id = p)
    data_op = Task(id =p)
    data_op.delete()
    return redirect('data')

#Register User
def Register(request):
	if request.method=='POST':
		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password']
		if password1==password1:
			if User.objects.filter(username = username).exists():
				messages.info(request , "Username already taken")
				return redirect('register')
			elif User.objects.filter(email = email).exists():
				messages.info(request,"email already exist")
				return redirect('register')
			else:
				user = User.objects.create_user(username = username , email=email , password=password1 )
				user.save()
				return redirect('data')
	return render(request , 'index.html')

#login view.....
def Login(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password1']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request , user)
			return redirect('data')
		else:
			messages.success(request, ('invalid credentials problem in login'))
			return redirect('login')
	return render(request,'login.html')

# Logout view... 
def logout(request):
	auth.logout(request)
	return redirect('login')




