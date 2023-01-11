from django.shortcuts import render

# Create your views here.


def page_one(request):
    return render (request, 'page_one.html')