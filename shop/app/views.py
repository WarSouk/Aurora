from app.forms import UserCreationForm, AddPoolForm
from app.models import *
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def academy(request):
    if request.method == 'POST':
        form = Pool(name=request.POST["name"],elo=request.POST["elo"], hours=request.POST["hours"],
                    nickname=request.POST["nickname"], discord=request.POST["discord"],
                    age=request.POST["age"], )
        form.save()
    return render(request, 'academy.html')


class UserRegister(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


def register_user(request):
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = User.objects.create_user(name=name, surname=surname, username=username, email=email, password=password)
    user.save
    return user
