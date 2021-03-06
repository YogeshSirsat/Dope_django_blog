from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='Dope_blog/login.html'), name='login'),


    path('reset/',
         auth_views.PasswordResetView.as_view(
             template_name='Dope_blog/password_reset.html',
             email_template_name='Dope_blog/password_reset_email.html',
             subject_template_name='Dope_blog/password_reset_subject.txt'
         ),
         name='password_reset'),

    path('reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='Dope_blog/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='Dope_blog/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='Dope_blog/password_reset_complete.html'),
         name='password_reset_complete'),

    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='Dope_blog/password_change.html'),
         name='password_change'),

    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='Dope_blog/password_change_done.html'),
         name='password_change_done'),

#     path('settings/account/',
#          views.UserUpdateView.as_view(), name='my_account'),
    path('settings/account/',
         views.Account, name='account'),


    path('likes', views.articlelikes, name='articlelike'),
    path('search', views.search, name='search'),
    path('articles/<str:category>/', views.articles, name='articles'),
    path('post/<int:id>-<str:slug>', views.post, name='post'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
# #     path('<str:room_name>/', views.room, name='room'),
]
