from django.http import HttpResponseNotFound,HttpResponse
from django.utils.timezone import now
import pytz # To specify Timezone
import logging



class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_time = now()
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
        if ip_address:
            ip_address = ip_address.split(',')[0]
        else:
            ip_address = request.META.get('REMOTE_ADDR')
        # print(f'Your IP address is: {ip_address}')
        # Creating an object
        #logger = logging.getLogger()
        # Setting the threshold of logger to DEBUG
        # logger.setLevel(logging.DEBUG)
        logging.warning("Warning log")


        request.ip_address = ip_address
        request.request_time = request_time
        # Call the next middleware or view
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        print(exception)
