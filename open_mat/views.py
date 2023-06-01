from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Notice
from django.shortcuts import render, get_object_or_404
from .forms import NoticeForm

def notice_list(request):
    notices = Notice.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'open_mat/notice_list.html', {'notices':notices})

def notice_detail(request, pk):
    Notice.objects.get(pk=pk)
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, 'open_mat/notice_detail.html', {'notice': notice})

def notice_new(request):
    if request.method == "POST":
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.author = request.user
            notice.published_date = timezone.now()
            notice.save()
            return redirect('notice_detail', pk=notice.pk)
    else:
        form = NoticeForm()
    return render(request, 'open_mat/notice_edit.html', {'form': form})

def notice_edit(request, pk):
    post = get_object_or_404(Notice, pk=pk)
    if request.method == "POST":
        form = NoticeForm(request.POST, instance=post)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.author = request.user
            notice.published_date = timezone.now()
            notice.save()
            return redirect('notice_detail', pk=notice.pk)
    else:
        form = NoticeForm(instance=post)
    return render(request, 'open_mat/notice_edit.html', {'form': form})