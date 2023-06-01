from django.shortcuts import render
from django.utils import timezone
from .models import Notice
from django.shortcuts import render, get_object_or_404

def notice_list(request):
    notices = Notice.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'open_mat/notice_list.html', {'notices':notices})

def notice_detail(request, pk):
    Notice.objects.get(pk=pk)
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, 'open_mat/notice_detail.html', {'notice': notice})