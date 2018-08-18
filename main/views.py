 # -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from main.models import DjangoBoard


def index(request):
    return render(request, 'main.html',{})


rowsPerPage=5
def show_post_list(request):
    boardList = DjangoBoard.objects.order_by('-id')[0:5]
    current_page = 1
    totalCnt = DjangoBoard.objects.all().count()

    pagingHelperIns = pagingHelper()

    totalPageList = pagingHelper.getTotalPageList(pagingHelperIns,totalCnt,rowsPerPage)
    print("totalPageList ", totalPageList)
    return render_to_response('boardMain.html', {'boardList':boardList, 'totalCnt': totalCnt ,
                                                        'current_page':current_page, 'totalPageList':totalPageList})

class pagingHelper:
    def getTotalPageList(self,total_cnt, rowsPerPage):
        if(total_cnt%rowsPerPage ==0):
            self.total_pages=total_cnt/rowsPerPage
            print('getTotalPage #1')

        else:
            self.total_pages = (total_cnt/rowsPerPage)+1;
            print('getTotalPage #2')

        self.totalPageList = []
        for i in range(self.total_pages):
            self.totalPageList.append(i+1)

        return self.totalPageList

    def __init__(self):
        self.total_pages = 0
        self.totalPageList = 0

def show_write_form(request):
    page_title = 'Write a post'
    return render(request, 'boardWrite.html',{ 'page_title' :page_title} )

def add_post(request):
    
    if request.POST.has_key('name') ==False:
	return HttpResponse('당신은 외계인인가요! 이름이 뭐에요!')
    else:
	if len(request.POST['name']) ==0:
	    return HttpResponse('이름이 null이신가요 그치만 그건 별로!')
	else:
	    entry_name = request.POST['name']


    if request.POST.has_key('title') ==False:
	return HttpResponse('제목이 울고 있어요! 만들어주세요!')
    else:
	if len(request.POST['title']) ==0:
	    return HttpResponse('제목이 너무 가난해요! 한톨이라도 적어주세요')
	else:
	    entry_title = request.POST['title']

    if request.POST.has_key('contents')==False:
	return HttpResponse('내용이 울고 있어요! 만들어주세요!')
    else:
	if len(request.POST['contents']) ==0:
	    return HttpResponse('내용이 너무 가난해요! 한톨이라도 적어주세요')
	else:
	    entry_contents = request.POST['contents']

    new_entry = DjangoBoard(subject= entry_title, contents=entry_contents, name = entry_name)
    
    try:    
	new_entry.save()
    except:
	return HttpResponse('미안합니다 데헤헤 글이 안 올라갈 것 같습니다!')
    
    return HttpResponse('고생하셨습니다! 글이 올라갔습니다루  뚜따띠!')
 
def show_read_form(request, pk):
    post = DjangoBoard.objects.get(pk=pk)
    return render(request, 'boardRead.html', {
        'post':post
    })

