import logging
import datetime

from django.http import HttpResponseForbidden
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse

from project.settings import GOLD, SILVER, BRONZE


logger = logging.getLogger(__name__)


class RateLimitMiddleware(MiddlewareMixin):
    def process_request(self, request):
        paths = [
            request.path.startswith(reverse("admin:index")),
            request.path.startswith(reverse("login")),
            request.path.startswith(reverse("register")),
            request.path.startswith(reverse("logout")),
        ]
        if any(paths):
            return self.get_response(request)

        user = request.user
        # pdb.set_trace()

        if user.is_authenticated:
            user_role = user.profile.role

            if user_role == "gold":
                rate_limit = GOLD
            elif user_role == "silver":
                rate_limit = SILVER
            elif user_role == "bronze":
                rate_limit = BRONZE
            else:
                rate_limit = 1

            ip = self.get_client_ip(request)
            profile = user.profile

            if profile.count == 0:
                profile.first_hit = timezone.now()
                response = self.set_fields(request, profile, ip)
                return response

            if timezone.now() < profile.first_hit + datetime.timedelta(minutes=1):
                if profile.count >= rate_limit:
                    # pdb.set_trace()
                    return HttpResponseForbidden("error: Rate limit exceeded")

                if profile.count > 0 and profile.count < rate_limit:
                    response = self.set_fields(request, profile, ip)
                    return response
            else:
                profile.count = 0
                profile.save()
                request.ip_address = ip
                request.request_time = profile.hit_time
                return self.get_response(request)
        else:
            return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

    def set_fields(self, request, profile, ip):
        profile.hit_time = timezone.now()
        profile.count = profile.count + 1
        profile.ip_address = ip
        profile.save()
        # This will be written to the file since the level is set to INFO
        logger.info(f"{ip} : {profile.hit_time} ")
        # Call the next middleware or view
        print(ip)
        request.ip_address = ip
        request.request_time = profile.hit_time

        updated = self.get_response(request)
        return updated
