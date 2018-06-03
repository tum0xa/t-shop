from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    success_html = '<div class="alert alert-success" role="alert"><i class="fa fa-check-circle-o"></i>The message with registration data has been sent!</div>'
    return HttpResponse(success_html)
