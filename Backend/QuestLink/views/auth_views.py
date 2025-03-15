from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

def login(request):
    pass

def logout(request):
    pass

def register(request):
    pass

@require_http_methods(["GET"])
def echo(request):
    return HttpResponse("Hello World!")
