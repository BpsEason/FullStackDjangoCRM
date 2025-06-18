from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Activity

@login_required
def activity_list(request):
    activities = Activity.objects.filter(created_by=request.user)
    return render(request, 'activities/activity_list.html', {'activities': activities})