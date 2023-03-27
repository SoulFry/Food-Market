from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, get_user_model, authenticate
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.http import HttpResponse, HttpResponseRedirect

from FoodSite import settings
from .token import account_activation_token
from .forms import *
from cafes.models import *
from orders.models import *
from main.models import User

User = get_user_model()

def index(request):
    establishments = Cafe.objects.all()
    most_popular = []
    for cafe in establishments:
        mark = cafe.get_total_mark
        if len(most_popular) < 6:
            most_popular.append(mark)
        else:
            if mark > min(most_popular):
                most_popular.remove(min(most_popular))
                most_popular.append(mark)
    most_popular_cafes = []
    for cafe in establishments:
        if cafe.get_total_mark in most_popular:
            most_popular_cafes.append(cafe)
    contex = {
        'cafes':most_popular_cafes
    }
    return render(request, 'main.html', contex)


class Authenfication:

    def activate(request, uidb64, token):
        try:
            uid = force_bytes(urlsafe_base64_decode(uidb64))
            user = User.object.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.is_confirmed = True
            user.save()
            return redirect('activated')
        else:
            return HttpResponse('Activation link is invalid!')

    def activated(request):
        return render(request, 'authenfication/activate.html')

    def register(request):
        if request.method == 'POST':
            form = UserRegistration(request.POST)
            if form.is_valid():
                useremail = form.cleaned_data['email']
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                login(request, user)
                current_site = get_current_site(request)
                email_subject = 'Ссылка для подтверждения регистрации'
                message = render_to_string('authenfication/activate_message.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                email = EmailMessage(
                    email_subject, message, to=[useremail]
                )
                email.send()
                messages.success(request, "Письмо с подтверждением было отправлено на указанную вами электронную почту")
            else:
                form = UserRegistration()
                messages.error(request, "Указанные данные не соответствуют требованиям")
        else:
            form = UserRegistration()
        return render(request, "authenfication/registration.html", {'form': form})

    def user_login(request):
        if request.method == 'POST':
            form = UserLogin(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('main')
            else:
                messages.error(request, 'Неверные данные')
                form = UserLogin()
        else:
            form = UserLogin()
        return render(request, "authenfication/login.html", {'form': form})


class Profile:
    def profile_panel(request):
        return render(request, 'profile.html')

    def avatar_change(request):
        if request.method == 'POST':
            form = UserAvatarChange(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                avatar = request.FILES
                if avatar is not None:
                    form.save()
                    return redirect('profile')
                else:
                    messages.error(request, 'Необходимо загрузить изображение')
                    form = UserAvatarChange()
            else:
                messages.error(request, 'Невозможно установить это изображение в качестве аватара')
                form = UserAvatarChange()
        else:
            form = UserAvatarChange()
        return render(request, 'profile/avatar-change.html', {'form': form})

    def password_check(request):
        if request.method == 'POST':
            form = PasswordCheck(request.POST)
            if form.is_valid():
                user = request.user
                old_password=form.cleaned_data['old_password']
                if user.check_password(old_password):
                    return redirect('password_change')
                else:
                    messages.error(request, 'Введён неверный пароль')
                    form = PasswordCheck()
            else:
                messages.error(request, 'Пароль не прошёл проверку')
                form = PasswordCheck()
        else:
            form = PasswordCheck()
        return render(request, 'profile/confirm-password.html', {'form':form})

    def password_change(request):
        if request.method == 'POST':
            form = PasswordChange(request.POST)
            if form.is_valid():
                user = request.user
                new_password2 = form.cleaned_data['new_password2']
                new_password = form.cleaned_data['new_password']
                if new_password == new_password2:
                    if not user.check_password(new_password):
                        user.set_password(new_password)
                        if not user.is_confirmed:
                            user.is_confirmed = True
                        user.save()
                        login(request, user)
                        return redirect('profile')
                    else:
                        messages.error(request, 'Пароль совпадает со старым паролем')
                        form = PasswordChange()
                else:
                    messages.error(request, 'Пароли не совпадают')
                    form = PasswordChange()
            else:
                messages.error(request, 'Пароль не прошёл проверку')
                form = PasswordChange()
        else:
            form = PasswordChange()
        return render(request, 'profile/password-change.html', {'form':form})

    def email_check(request):
        if request.method == "POST":
            form = EmailCheck(request.POST)
            if form.is_valid():
                use_mail = form.cleaned_data['email']
                try:
                    user = User.object.get(email=use_mail)
                except(TypeError, ValueError, OverflowError, User.DoesNotExist):
                    user = None
                if user is not None:
                    current_site = get_current_site(request)
                    email_subject = 'Ссылка для сброса пароля'
                    message = render_to_string('profile/password-reset-message.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': account_activation_token.make_token(user),
                        'email': use_mail
                    })
                    email = EmailMessage(
                        email_subject, message, to=[use_mail]
                    )
                    email.send()
                    messages.success(request, "Письмо для сброса пароля было отправлено на вашу почту")
                else:
                    messages.error(request, 'Пользователя с такой почтой не зарегистрирован')
            else:
                messages.error(request, 'Ошибка в введённой почте')
                form = EmailCheck()
        else:
            form = EmailCheck()
        return render(request, 'profile/password-reset.html', {'form': form})

    def password_change_check(request, uidb64, token, email):
        try:
            uid = force_bytes(urlsafe_base64_decode(uidb64))
            user_decode = User.object.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user_decode = None
        if user_decode is not None and account_activation_token.check_token(user_decode, token):
            user = User.object.get(email=email)
            user.is_confirmed = False
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('password_change')
        else:
            return HttpResponse('Неверная ссылка!')

    def user_history(request):
        user = request.user
        orders = Order.objects.filter(user=user)
        order_elements = ItemsInOrder.objects.all()
        contex = {
            'orders': orders,
            'order_element': order_elements
        }
        return render(request, 'profile/history.html', contex)
