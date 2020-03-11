# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse
from django.http import JsonResponse
from pyhanlp import *


def summary(request):
    content = request.POST.get('content')
    if content:
        TextRankSentence = JClass("com.hankcs.hanlp.summary.TextRankSentence")
        sentence_list = HanLP.extractSummary(content, 2)
        keyword = HanLP.extractKeyword(content, 5)
        sentence = str(sentence_list)[1:-1].split(', ')
        # for s in sentence:
        #     if len(s) >= 25:
        #         s = s[:24]
        keyword_list = str(keyword)[1:-1].split(', ')
        data = {
            'summary': sentence,
            'keyword': keyword_list
        }
        return JsonResponse(data)
