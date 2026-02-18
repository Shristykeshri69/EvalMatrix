"""
URL configuration for EvalMatrix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from exams import views
from exams.views import CustomLoginView
from exams.views import register_view


urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    

    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),

    # Home
    path('', views.home_page_view, name='home'),

    # Dynamic Exam Start
    path('exam/<int:exam_id>/', views.start_exam, name='start_exam'),

    # Logout (if custom)
    path('logout/', views.logout_view, name='logout'),

    path('my-results/', views.my_results, name='my_results'),

    path('log-activity/', views.log_activity, name='log_activity'),

    path('register/', register_view, name='register'),



]






