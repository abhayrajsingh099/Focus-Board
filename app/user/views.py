"""
User authentication logic views.
"""

from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import get_user_model, authenticate, login ,logout

from .forms import RegisterForm


User = get_user_model()


# def regsiterView(request):

#     if request.method == 'POST':
#         form = RegisterForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect('user:login')
#         else:
#             messages.error(request, f"{form.errors}")
#             return redirect('user:register')
#     else:
#         form = RegisterForm()

#     return render(request, 'register.html', {'form':form})


# def loginView(request):

#     form = LoginForm()

#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)

#         if user:
#             login(request, user)
#             messages.success(request, f"{user} Logged In!!")
#             return redirect('tasks:list_task')
#         else:
#             messages.error(request, f"{form.errors}")
#             return redirect('user:login')

    # return render(request, 'login.html', {'form':form})

# def logoutView(request):
#     user = request.user

#     logout(request)
#     messages.success(request, f"{user} Logged Out!!")

#     return redirect('user:login')



