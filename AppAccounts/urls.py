from django.urls import path
from .views import account,Teacher1,TeacherAccount

urlpatterns=[
    path("",account,name="account"),
    path("teacher/",Teacher1.as_view(),name="teacher"),
    path("teacher/<int:pk>",TeacherAccount.as_view(),name="teacher_ac")
]