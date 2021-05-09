from django.urls import path,reverse_lazy
from . import views
from django.contrib.auth import views as imp_views

app_name = 'accounts'

urlpatterns = [
    path("login/",imp_views.LoginView.as_view(template_name='registrations/login.html'),name='login'),
    path("logout/",imp_views.LogoutView.as_view(),name='logout'),
    path("register/",views.register.as_view(),name='signup'),
    path("password-reset/",imp_views.PasswordResetView.as_view(template_name='registrations/password_reset_form.html',
                                                                email_template_name='registrations/password_reset_email.html',
                                                                subject_template_name='registrations/password_reset_subject.txt',
                                                                from_email="mohammedfarhan045@gmail.com",
                                                                success_url =reverse_lazy('accounts:password_reset_done')),name='password_reset'),
    path("password-reset/done/",imp_views.PasswordResetDoneView.as_view(template_name='registrations/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', imp_views.PasswordResetConfirmView.as_view(template_name='registrations/password_reset_confirm.html',
                                                                                success_url=reverse_lazy("accounts:password_reset_complete")), name='password_reset_confirm'),
    path("password-reset/complete/",imp_views.PasswordResetCompleteView.as_view(template_name='registrations/password_reset_complete.html'),name='password_reset_complete'),
    path("All-users/",views.Allusers,name="all_users"),
]
