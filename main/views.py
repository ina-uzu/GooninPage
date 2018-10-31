# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse

from .forms import UserForm, LoginForm

from django.contrib.auth import login, authenticate
from main.models import DjangoBoard, Letters


def index(request):
    return render(request, 'main.html', {})


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')
        else:
            return redirect('join')
    else:
        form = UserForm()
        return render(request, 'join.html', {'form': form})


def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요:(')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


rowsPerPage = 5


def show_post_list(request):
    boardList = DjangoBoard.objects.order_by('-id')[0:5]
    current_page = 1
    totalCnt = DjangoBoard.objects.all().count()

    pagingHelperIns = pagingHelper()

    totalPageList = pagingHelper.getTotalPageList(pagingHelperIns, totalCnt, rowsPerPage)
    print("totalPageList ", totalPageList)
    return render_to_response('boardMain.html', {'boardList': boardList, 'totalCnt': totalCnt,
                                                 'current_page': current_page, 'totalPageList': totalPageList})


class pagingHelper:
    def getTotalPageList(self, total_cnt, rowsPerPage):
        if (total_cnt % rowsPerPage == 0):
            self.total_pages = total_cnt / rowsPerPage
            print('getTotalPage #1')

        else:
            self.total_pages = (total_cnt / rowsPerPage) + 1;
            print('getTotalPage #2')

        self.totalPageList = []

        for i in range(int(self.total_pages)):
            self.totalPageList.append(i + 1)

        return self.totalPageList

    def __init__(self):
        self.total_pages = 0
        self.totalPageList = 0


def show_write_form(request):
    page_title = 'Write a post'
    return render(request, 'boardWrite.html', {'page_title': page_title})


def add_post(request):
    if 'name' not in request.POST:
        return HttpResponse('당신은 외계인인가요! 이름이 뭐에요!')
    else:
        if len(request.POST['name']) == 0:
            return HttpResponse('이름이 null이신가요 그치만 그건 별로!')
        else:
            entry_name = request.POST['name']

    if 'title' not in request.POST:
        return HttpResponse('제목이 울고 있어요! 만들어주세요!')
    else:
        if len(request.POST['title']) == 0:
            return HttpResponse('제목이 너무 가난해요! 한톨이라도 적어주세요')
        else:
            entry_title = request.POST['title']

    if 'contents' not in request.POST:
        return HttpResponse('내용이 울고 있어요! 만들어주세요!')
    else:
        if len(request.POST['contents']) == 0:
            return HttpResponse('내용이 너무 가난해요! 한톨이라도 적어주세요')
        else:
            entry_contents = request.POST['contents']

    new_entry = DjangoBoard(subject=entry_title, contents=entry_contents, name=entry_name)

    try:
        new_entry.save()
    except:
        return HttpResponse('미안합니다 데헤헤 글이 안 올라갈 것 같습니다!')

    return HttpResponse('고생하셨습니다! 글이 올라갔습니다루  뚜따띠!')


def show_read_form(request, pk):
    post = DjangoBoard.objects.get(pk=pk)
    return render(request, 'boardRead.html', {
        'post': post
    })


def show_schd(request):
    return render(request, 'schdMain.html')


def show_letters(request):
    return render(request, 'letterWrite.html')


def send_letters(request):
    if 'sender' not in request.POST:
        return HttpResponse('보내는 사람은 외계인인가요! 이름이 뭐에요!')
    else:
        if len(request.POST['sender']) == 0:
            return HttpResponse('보내는 사람이 null이신가요 그치만 그건 별로!')
        else:
            entry_sender = request.POST['sender']

    if 'receiver' not in request.POST:
        return HttpResponse('받는 사람은 외계인인가요! 이름이 뭐에요!')
    else:
        if len(request.POST['receiver']) == 0:
            return HttpResponse('받는 사람이 null이신가요 그치만 그건 별로!')
        else:
            entry_receiver = request.POST['receiver']

    if 'contents' not in request.POST:
        return HttpResponse('우표값이 아까워요! 내용을 적어주세요!')
    else:
        if len(request.POST['contents']) == 0:
            return HttpResponse('우표값이 아까워요! 내용을 적어주세요!')
        else:
            entry_contents = request.POST['contents']

    new_entry = Letters(sender=entry_sender, receiver=entry_sender, contents=entry_contents)

    try:
        new_entry.save()
    except:
        return HttpResponse('미안합니다 데헤헤 편지가 안 보내질 것 같습니다!')

    return HttpResponse('고생하셨습니다! 편지가 보내졌어요! 뚜따띠!')
