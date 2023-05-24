from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.
from .models import Teacher


def account(request):
    return HttpResponse("Bu account page")


class Teacher1(ListView):
    model = Teacher
    template_name = "teacher.html"
    context_object_name = "teachers_list"


class TeacherAccount(DetailView):
    model = Teacher
    template_name = "teacher_ac.html"
    context_object_name = "object"
