from django.shortcuts import  render
from . models import place
# Create your views here.

def demo(request):
    obj=place.objects.all()
    return  render(request,"index.html",{"results":obj})








# def register(request):
#     if request.method== 'POST':
#         username=request.POST['username']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password = request.POST['password']
#         cpassword = request.POST['password1']
#         user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
#         user.save();
#         print("user created")
#
#     return  render(request,"register.html")
# def demo(request):
#     obj=place.objects.all()

