

"""
здесь будет коментарий , а пока Артем баран
"""

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Артем повелитель питона")
