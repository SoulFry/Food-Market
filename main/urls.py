from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('logout', LogoutView.as_view(), name='logout'),

    path('authenfication/registration', Authenfication.register, name='registration'),
    path('authenfication/login', Authenfication.user_login, name='login'),
    path('authenfication/activate', Authenfication.activated, name='activated'),
    path('authenfication/activate/<uidb64>/<token>', Authenfication.activate, name='activate'),

    path('profile', Profile.profile_panel, name = 'profile'),
    path('profile/avatar_change', Profile.avatar_change, name='avatar_change'),
    path('profile/password-confirm', Profile.password_check, name='password_check'),
    path('profile/password-change', Profile.password_change, name='password_change'),
    path('profile/password-reset', Profile.email_check, name='password-reset'),
    path('profile/password-change/<uidb64>/<token>/<email>', Profile.password_change_check, name='password-reset-check'),
    path('profile/history', Profile.user_history, name='history')
]