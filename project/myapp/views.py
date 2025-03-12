from django.shortcuts import render,HttpResponse
import logging


# logging.basicConfig(
#     filename="newfile.log",
#     encoding='utf-8',
#     format="{asctime} - {levelname} - {message}",
#     style="%",
# )
# logger = logging.getLogger()


def get_user_ip(request):
   ip_address = getattr(request,'ip_address',"None")
   request_time = getattr(request,'request_time','00-00-00')

   #    # Creating an object
   # # Setting the threshold of logger to DEBUG
   # logger.setLevel(logging.DEBUG)
   # logging.debug(f"{request_time}: {ip_address}:")

   context = {
      "ip_address" : ip_address
   }

   return HttpResponse(f"IP from view: {ip_address} at time {request_time}")
