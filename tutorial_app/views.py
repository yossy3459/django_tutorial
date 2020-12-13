from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if 'msg' in request.GET:
        msg = request.GET['msg']
        res = f"Query Param.: {msg}"
    else:
        res = f"Query: not respond"

    return HttpResponse(res)

def information(request, id, name, age):
    res = f"Your name: {name}, Your id: {id}, Your age: {age}"
    return HttpResponse(res)