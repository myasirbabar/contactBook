from . import views
from django.urls import path

urlpatterns = [
    path('', views.index_view, name='index-view'),
    path('loginuser', views.login_user, name='login-user'),
    path('error', views.error, name='error'),
    path('logout', views.logout, name='logout'),
]
