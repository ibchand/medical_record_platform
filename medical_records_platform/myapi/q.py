from time import sleep
from django.http import JsonResponse

def q_stub_func(json_payload, sleep_sec):
    sleep(sleep_sec)
    return JsonResponse(json_payload)