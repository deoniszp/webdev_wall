from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(["GET"])
def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        return render(request, 'app_auth/login.html')

@require_http_methods(["GET"])
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")