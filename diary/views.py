from django.shortcuts import render, redirect
from diary.models import Diary
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def diary_main(request):
    diaries = Diary.objects.all().order_by('-id')
    num = len(diaries)
    ctx = {
        'num': num
    }
    return render(request, 'diary/diary_main.html', ctx)


@login_required(login_url='/account/login/')
def diary_list(request):
    diaries = Diary.objects.all().order_by('-id')
    ctx = {
        'diaries': diaries,
    }
    return render(request, 'diary/diary_list.html', ctx)


@login_required(login_url='/account/login/')
def diary_detail(request, pk):
    diary = Diary.objects.get(id=pk)
    ctx = {
        'diary': diary
    }
    return render(request, 'diary/diary_detail.html', ctx)


@login_required(login_url='/account/login/')
def diary_create(request):
    if request.method == 'GET':
        return render(request, 'diary/diary_create.html')
    else:
        new_diary = Diary()
        new_diary.title = request.POST['title']
        new_diary.content = request.POST['content']
        try:
            if request.FILES['image']:
                new_diary.image = request.FILES['image']
        except:
            pass
        new_diary.save()

        pk = new_diary.id
        diary = Diary.objects.get(id=pk)
        ctx = {
            'diary': diary
        }
        return render(request, 'diary/diary_detail.html', ctx)


@login_required(login_url='/account/login/')
def diary_update(request, pk):
    if request.method == 'GET':
        diary = Diary.objects.get(id=pk)
        ctx = {
            'diary': diary
        }
        return render(request, 'diary/diary_update.html', ctx)
    else:
        update_diary = Diary.objects.get(id=pk)
        update_diary.title = request.POST['title']
        update_diary.content = request.POST['content']
        try:
            if request.FILES['image']:
                update_diary.image = request.FILES['image']
        except:
            pass
        update_diary.save()

        diary = Diary.objects.get(id=pk)
        ctx = {
            'diary': diary
        }
        return render(request, 'diary/diary_detail.html', ctx)


@login_required(login_url='/account/login/')
def diary_delete(request, pk):
    if request.method == 'GET':
        return redirect('/diary')
    else:
        diary = Diary.objects.get(id=pk)
        diary.delete()
        return redirect('/diary')
