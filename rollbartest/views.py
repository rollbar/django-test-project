from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world')


def error(request):
    # foo()
    return HttpResponse('Default Error Response')
