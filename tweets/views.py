# Function-based view

'''
from django.http import HttpResponse

def index(request):
    if request.method =='GET':
        return HttpResponse('I am called from a get Request')
    elif request.method == 'POST':
        return HttpResponse('I am called from a post Request')

#Class-based view:
from django.http import HttpResponse
from django.views.generic import View

class Index(View):
    def get(self,request):
        return HttpResponse('I am called from a class based get Request')
    def post(self,request):
        return HttpResponse('I am called from a class based ßpost Request')

'''

from django.views.generic import View
from django.shortcuts import render
class Index(View):
    def get(self, request):
        params = {}
        params["name"] = "Django"
        return render(request, 'base.html', params)
