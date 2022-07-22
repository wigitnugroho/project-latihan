from django.http import HttpResponse
from django.shortcuts import render

#method view


def index(request):
  context = {
    'title' : 'kelas terbuka',
    'heading' : 'selamat datang',
    'subheading' : 'di kelas terbuka'
  }
  return render(request,'index.html' ,context)

def about(request):
    return HttpResponse("<h1>ini about<?h1>")