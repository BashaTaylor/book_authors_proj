from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, index.html)

# def validate_login(request):
#     user = User.objects.get(email=request.POST['email'])  # hm...is it really a good idea to use the get method here?
#     if bcrypt.checkpw(request.POST['password'].encode(), user.pw_hash.encode()):
#         print("password match")
#     else:
#         print("failed password")   