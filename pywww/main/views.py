# from django.shortcuts import render -deleted
from django.http import HttpResponse

# Create your views here.
def hello_word(request):
  return HttpResponse("Hello Word!")