from django.shortcuts import render
from .models import Store

def index(request):
    stores = Store.objects.all()
    return render(request, 'stores/index.html', {'stores': stores})
