from django.shortcuts import render
from django.http import HttpResponse
from data.models import Area_Course
from data.models import College

def index(request):
    area_courses = Area_Course.objects.all()
    return render(request,"index.html",{ 'items':area_courses})
