from django.shortcuts import render
from .models import Roll

# Create your views here.


def rolls(request):
    rolls = Roll.objects.all()
    return render(request, 'rolls/sushi-rolls.html', {'rolls': rolls})


def contactUs(request):
    return render(request, 'rolls/contact-us.html')
