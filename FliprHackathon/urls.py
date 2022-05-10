"""FliprHackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BankProfile import views as profile_views
from user import views as user_views
import FliprHackathon.views as root_views
import loans.views as loan_views
import request_loan.views as req_loan_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',root_views.home,name="home"),
    path('register/',user_views.register,name="register"),
    path('user/profile',user_views.UpdateProfile,name="user_profile"),
    path('login/',auth_views.LoginView.as_view(template_name="users/login.html"),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name="users/logout.html"),name="logout"),
    path('profile/dashboard',profile_views.dashboard,name="dashboard"),
    path('profile/bank_profile',profile_views.bank_profile,name="bank_profile"),
    path('loan/loan_view',loan_views.loan_view,name="loan_view"),
    path('loan/apply_loan',loan_views.apply_loan,name="apply_loan"),
    path('loan/dashboard',loan_views.loan_dashboard,name="loan_dashboard"),
    path('loan/accept/<int:pk>',loan_views.accept,name="loan_accept"),
    path('loan/delete/<int:pk>',loan_views.delete,name="loan_delete"),
    path('loan/modify/<int:pk>',loan_views.modify,name="loan_modify"),
    path('req_loan/modify_request/<int:pk>',req_loan_view.modify_request,name="loan_modify_request"),
    path('req_loan/modify_request_view/<int:pk>',req_loan_view.modify_request_view,name="modify_request_view"),
    path('req_loan/accept_req/<int:pk>',req_loan_view.accept_modify,name="accept_request"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)