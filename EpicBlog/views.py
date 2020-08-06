from django.shortcuts import render


def cookie(request):
    return render(request, 'cookie.html', {})
