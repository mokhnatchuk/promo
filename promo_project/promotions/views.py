from django.shortcuts import render
from .models import Promotion

def index(request):
    promotions = Promotion.objects.all()
    return render(request, 'promotions/index.html', {'promotions': promotions})
