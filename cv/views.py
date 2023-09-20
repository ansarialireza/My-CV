from django.shortcuts import render
from .models import UserProfile

def index(request):
    profiles = UserProfile.objects.all()
    return render(request, 'index.html', {'profiles': profiles})
