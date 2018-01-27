from django.shortcuts import render
from .forms import TestForm
# Create your views here.

def test_app_view(request):
    form = TestForm()
    return render(request, 'testapp/index.html', {'form':form})
