from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Batch
# Create your views here.

def index(request):
    all_batches = Batch.objects.all()
    return render(request, 'batch/index.html', {'all_batches': all_batches})

def batch_students(request, batch_id):
    batch = get_object_or_404(Batch, pk = batch_id)
    return render(request, 'batch/batch_students.html', {'batch':batch})

