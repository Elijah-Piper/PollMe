from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	"""Homepage"""
	return HttpResponse("Hello, world. You're at the polls index.")