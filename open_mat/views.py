from django.shortcuts import render
from django.utils import timezone
from .models import Notice

def post_list(request):
    notices = Notice.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'open_mat/notice_list.html', {'notices':notices})