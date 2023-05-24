import json

from django.shortcuts import render
from django.views.generic import TemplateView,ListView
# Create your views here.
from AppAccounts.models import Teacher
from django.http import HttpResponse,JsonResponse


def index(request):
    context={}
    return render(request,template_name="index.html",context=context)

def api(request):
    teachers={"dfsdf":"dsfs"}
    return JsonResponse({"data":teachers})