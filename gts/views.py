from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")

def privacy(request):
    return HttpResponse("My privacy policy here.")
