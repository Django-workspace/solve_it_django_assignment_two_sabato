from ast import If
from multiprocessing import context
from urllib import request
from django.http import HttpResponse,Http404
from django.shortcuts import render
from django.http import HttpResponse
from firstapp.forms import TraineeForm

from firstapp.models import Trainee
# Create your views here.

def index(request):
    trainees = Trainee.objects.all()

    form = TraineeForm(request.POST)

    if form.is_valid():
        form.save()

    context = {
        'trainees':trainees,
        'form':form
    }


    return render(request,'index.html',context)

def delete(request,trainee_id):
    context = {
        'status':"Traine deleted"
    }
    try:
        trainee = Trainee.objects.filter(id=trainee_id).delete()
    except Trainee.DoesNotExist:
        raise Http404("Trainee you are deleting does not exist")
    return render(request,'deleted.html',context)

# def create(context):

# def edit(request,trainee_id):


    