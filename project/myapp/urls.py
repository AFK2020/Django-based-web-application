from django.urls import path
from .views import CustomLoginView, CustomLogoutView, RegisterPage, get_user_ip


urlpatterns = [
    path("get-ip/", get_user_ip, name="get-ip"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", RegisterPage.as_view(), name="register"),
]
