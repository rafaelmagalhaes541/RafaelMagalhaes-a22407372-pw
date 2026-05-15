from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import RegistoForm

# Create your views here.
# LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            return render(request, 'accounts/login.html', {
                'erro': 'Credenciais inválidas'
            })

    return render(request, 'accounts/login.html')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('home')


# REGISTO
def registo_view(request):
    if request.method == 'POST':
        form = RegistoForm(request.POST)
        if form.is_valid():
            user = form.save() 

            grupo, created = Group.objects.get_or_create(name='autores')
            user.groups.add(grupo)

            return redirect('login')
    else:
        form = RegistoForm()

    return render(request, 'accounts/registo.html', {'form': form})

def login_magic_link(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)

            user.token = secrets.token_urlsafe(32)
            user.save()

            link = request.build_absolute_uri(
                f"/accounts/magic-login/?token={user.token}"
            )

            print("MAGIC LINK:", link)

            return render(request, 'accounts/magic_sent.html', {'link': link})

    return render(request, 'accounts/magic_form.html')

def magic_login(request):
    token = request.GET.get('token')

    user = User.objects.filter(token=token).first()

    if user:
        login(request, user)

        user.token = None
        user.save()

        return redirect('portfolio')

    return render(request, 'accounts/magic_invalid.html')
