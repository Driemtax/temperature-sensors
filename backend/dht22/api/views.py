from django.http import JsonResponse

# Create your views here.
def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "You successfully reached the api over your local network!"})