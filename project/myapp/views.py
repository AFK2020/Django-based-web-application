from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# from django_ratelimit.decorators import ratelimit
# @ratelimit(key='ip', rate='5/m')
@login_required(login_url="/login/")
def get_user_ip(request):
    ip_address = getattr(request, "ip_address", "None")
    request_time = getattr(request, "request_time", "00-00-00")
    context = {
        "ip_address": ip_address,
        "request_time": request_time,
        "email": request.user.email,
    }
    return render(request, "myapp/ip.html", context=context)


class CustomLoginView(LoginView):
    template_name = "myapp/login.html"
    redirect_authenticated_user = (
        True  # if user is authenticated then don't bring it back to this page
    )

    def get_success_url(self):
        return reverse_lazy("get-ip")


class CustomLogoutView(LogoutView):
    http_method_names = ["get", "post", "options"]
    next_page = reverse_lazy("login")

    def get(self, request, *args, **kwargs):
        logout(request)  # Log out the user
        return redirect("login")


class RegisterPage(FormView):
    template_name = "myapp/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("get-ip")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("get-ip")
        return super(RegisterPage, self).get(*args, **kwargs)
