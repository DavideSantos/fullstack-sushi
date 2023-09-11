from django.shortcuts import render

# Create your views here.


def rolls(request):
    return render(request, 'rolls/sushi-rolls.html')
