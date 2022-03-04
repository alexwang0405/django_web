from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.sign_out, name='logout'),
    path('punch/<clock_type>', views.punch, name='punch'),
]