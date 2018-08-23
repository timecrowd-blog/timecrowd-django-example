from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    user = request.user
    timecrowd_user = user.social_auth.get(provider='timecrowd')
    #import pdb; pdb.set_trace()
    return render(request, 'dashboard.html', {
        'timecrowd_user': timecrowd_user,
    })
