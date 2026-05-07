from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegisterForm
from .models import MagicLinkToken
from django.contrib.auth.models import Group


def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error = 'Credenciais inválidas.'
    return render(request, 'accounts/login.html', {'error': error})

def logout_view(request):
    logout(request)
    return redirect('/')

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    return render(request, 'accounts/register.html', {'form': form})

def magic_link_request(request):
    error = None
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            token = MagicLinkToken.objects.create(user=user)
            link = request.build_absolute_uri(f'/accounts/magic-link/{token.token}/')
            send_mail(
                subject='O teu link de acesso',
                message=f'Clica aqui para entrar: {link}',
                from_email='noreply@portfolio.com',
                recipient_list=[email],
            )
            return render(request, 'accounts/magic_link_sent.html')
        except User.DoesNotExist:
            error = 'Não existe nenhuma conta com esse email.'
    return render(request, 'accounts/magic_link_request.html', {'error': error})

def magic_link_verify(request, token):
    try:
        magic = MagicLinkToken.objects.get(token=token)
        user = magic.user
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        magic.delete()
        return redirect('/')
    except MagicLinkToken.DoesNotExist:
        return render(request, 'accounts/magic_link_invalid.html')

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            grupo, _ = Group.objects.get_or_create(name='autores')
            user.groups.add(grupo)
            return redirect('accounts:login')
    return render(request, 'accounts/register.html', {'form': form})