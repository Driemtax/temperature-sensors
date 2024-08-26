from django.http import JsonResponse
from .temp import get_data

# Create your views here.
def api_home(request, *args, **kwargs):
    data = get_data()
    return JsonResponse(data)

def stats(request, *args, **kwargs):
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
        # Calculate in Celsius
        temp = int(file.read()) / 1000.0
    return JsonResponse({"temperature": temp})