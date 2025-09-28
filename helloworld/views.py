from django.http import HttpResponse
from django.conf import settings

def index(request):
    print(settings.ALLOWED_HOSTS)
    return HttpResponse("Hello, world! 2\n")
