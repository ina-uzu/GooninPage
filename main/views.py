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
    
#    template = get_template('boardWrite.html')
#    context = {
#	'page_title': page_title    }

    return render(request, 'boardWrite.html',{ 'page_title' :page_title} )

def add_post(request):
    entry_title = request.POST['title']
    return HttpResponse('hello %s' % entry_title)

def show_read_form(request, pk):
    post = DjangoBoard.objects.get(pk=pk)
    return render(request, 'boardRead.html', {
        'post':post
    })

