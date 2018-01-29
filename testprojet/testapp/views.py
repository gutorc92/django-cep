from django.utils.translation import gettext as _
from django.shortcuts import render
from django.views import View
from .forms import TestForm
# Create your views here.

class TestAppView(View):

    def get(self, request):
        form = TestForm()
        return render(request, 'testapp/index.html', {'form':form})

    def post(self, request):
        form = TestForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(requets, _("Test registered with sucess"))
        return render(request, 'testapp/index.html', {'form':form})

