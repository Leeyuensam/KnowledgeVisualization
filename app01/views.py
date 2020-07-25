from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app01.models import *
from app01.find_all_title import *

'''
    获取时间下的所有数据
    url: http://127.0.0.1:8000/knowledge
    请求形式：
    {
        "date": "2020/2/14"
    }
'''


class find_data(APIView):
    def post(self, request):
        date = request.data.get('date')
        papers_data = research_papers.objects.filter(date=date).values_list('title', 'authors', 'abstract', 'ents')
        news_data = news.objects.filter(date=date).values_list('title', 'content', 'source_url', 'ents')
        rumor_data = rumors.objects.filter(publish_date=date).values_list('rumor', 'fact', 'ents')
        json_list = []
        papers_dic = {}
        news_dic = {}
        rumors_dic = {}
        final_dic = {}
        for i in papers_data:
            title = i[0]
            authors_list = str(i[1]).split(',')
            ents_list = str(i[3]).split(',')
            papers_dic[title] = {
                'authors': authors_list,
                'abstract': i[2],
                'ents': ents_list
            }

        for i in news_data:
            title = i[0]
            ents_list = str(i[3]).split(',')
            news_dic[title] = {
                'content': i[1],
                'source_url': i[2],
                'ents': ents_list
            }

        for i in rumor_data:
            rumor = i[0]
            ents_list = str(i[2]).split(',')
            rumors_dic[rumor] = {
                'fact': i[1],
                'ents': ents_list
            }
        final_dic['papers'] = papers_dic
        final_dic['news'] = news_dic
        final_dic['rumors'] = rumors_dic
        json_list.append(final_dic)

        return Response(json_list)


'''
    标题获取所有数据  论文
    url: http://127.0.0.1:8000/title_find_paper_data
    请求形式：
    {
        "title": "China reopened wildlife markets."
    }
'''


class title_find_paper_data(APIView):
    def post(self, request):
        title = request.data.get('title')
        data = research_papers.objects.filter(title=title)
        json_list = []
        for i in data:
            authors_list = str(i.authors).split(',')
            ent_list = str(i.ents).split(',')
            json_list.append({
                'date': i.date,
                'title': i.title,
                'authors': authors_list,
                'abstract': i.abstract,
                'ents': ent_list
            })
        return Response(json_list)


'''
    标题获取所有数据  新闻
    url: http://127.0.0.1:8000/title_find_news_data
    请求形式：
    {
        "title": "China reopened wildlife markets."
    }
'''


class title_find_news_data(APIView):
    def post(self, request):
        title = request.data.get('title')
        data = news.objects.filter(title=title)
        json_list = []
        for i in data:
            ents_list = str(i.ents).split(',')
            json_list.append({
                'date': i.date,
                'title': i.title,
                'content': i.content,
                'source_url': i.source_url,
                'ents': ents_list
            })
        return Response(json_list)


'''
    标题获取所有数据  谣言
    url: http://127.0.0.1:8000/title_find_rumor_data
    请求形式：
    {
        "title": "China reopened wildlife markets."
    }
'''


class title_find_rumor_data(APIView):
    def post(self, request):
        title = request.data.get('title')
        data = rumors.objects.filter(rumor=title)
        json_list = []
        for i in data:
            ent_list = str(i.ents).split(',')
            json_list.append({
                'date': i.publish_date,
                'title': i.rumor,
                'fact': i.fact,
                'ents': ent_list
            })
        return Response(json_list)


'''
    标题获取相近的10条标题  论文
    url: http://127.0.0.1:8000/find_similar_paper_titles
    请求形式：
    {
        "title": "China reopened wildlife markets."
    }
'''


class find_similar_paper_titles(APIView):
    def post(self, request):
        target_title = request.data.get('title')
        findTitles = findAllTitle()
        title_data = research_papers.objects.all().values_list('title')
        title_list = []
        for i in title_data:
            title_list.append(i[0])
        json_list = findTitles.find_similar_title(target_title, title_list)
        print(len(title_list))
        return Response(json_list)


'''
    标题获取相近的10条标题  新闻
    url: http://127.0.0.1:8000/find_similar_news_titles
    请求形式：
    {
        "title": "China reopened wildlife markets."
    }
'''


class find_similar_news_titles(APIView):
    def post(self, request):
        target_title = request.data.get('title')
        findTitles = findAllTitle()
        title_data = news.objects.all().values_list('title')
        title_list = []
        for i in title_data:
            title_list.append(i[0])
        json_list = findTitles.find_similar_title(target_title, title_list)
        print(len(title_list))
        return Response(json_list)


'''
    标题获取相近的10条标题  谣言
    url: http://127.0.0.1:8000/find_similar_rumors_titles
    请求形式：
    {
        "title": "China reopened wildlife markets."
    }
'''


class find_similar_rumors_titles(APIView):
    def post(self, request):
        target_title = request.data.get('title')
        findTitles = findAllTitle()
        title_data = rumors.objects.all().values_list('rumor')
        title_list = []
        for i in title_data:
            title_list.append(i[0])
        json_list = findTitles.find_similar_title(target_title, title_list)
        print(len(title_list))
        return Response(json_list)
# Create your views here.
