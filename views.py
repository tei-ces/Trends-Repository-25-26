from django.shortcuts import render

def myfirst(request):
    return render(request, "members/myfirst.html")