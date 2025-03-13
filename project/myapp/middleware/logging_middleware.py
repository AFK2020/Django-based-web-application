from django.http import HttpResponseForbidden
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
from myapp.models import CustomUser, Profile
import logging

logger = logging.getLogger('myapp')


class RateLimitMiddleware(MiddlewareMixin):
    rate_limit = 500  # Number of allowed requests
    TIME_PERIOD = 60  # Time period in seconds

    def process_request(self, request):
        # if str(request.user) == 'AnonymousUser':
        #     self.rate_limit = 1

        ip, request_time = self.get_client_ip(request)
        key = f'rate-limit-{ip}'
        request_count = cache.get(key, 0)
        
        if request_count == 0:
            cache.set(key, 1, timeout=self.TIME_PERIOD)
            request_count = 1

        if request_count <= self.rate_limit:
            request_count = request_count+1
            request.ip_address = ip
            request.request_time = request_time
            cache.incr(key)
            # This will be written to the file since the level is set to INFO
            logger.info(f"{request.ip_address} : {request.request_time} ")
            # Call the next middleware or view
            response = self.get_response(request)
            return response
        
        if request_count >= self.rate_limit:
            return HttpResponseForbidden('error: Rate limit exceeded')

    def get_client_ip(self, request):
        request_time = timezone.now()

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip,request_time
