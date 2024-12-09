from django.shortcuts import render
from django.views.generic import UpdateView, ListView
from .models import subject

# Create your views here.
class Lsv(ListView):
    model = subject
    template_name = 'task_view.html'
    
class subjectupdate(UpdateView):
    model = subject
    fields = ['subject_name', 'subject_code']
    context_object_name = 'update'
    template_name = 'task_update.html'