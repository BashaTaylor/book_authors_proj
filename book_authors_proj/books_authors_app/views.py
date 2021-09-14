from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'my_home.html')

    # def create_user(request):
    # #1 create the user
    # new_user=User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'], age=request.POST['age'])
    # return redirect('/')