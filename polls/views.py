from django.http import HttpResponse

def page(request):
    return HttpResponse("Hello guys, this is a page!")
