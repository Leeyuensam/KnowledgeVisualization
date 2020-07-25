"""知识可视化 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app01.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('knowledge', find_data.as_view()),
    path('title_find_paper_data', title_find_paper_data.as_view()),
    path('title_find_news_data', title_find_news_data.as_view()),
    path('title_find_rumor_data', title_find_rumor_data.as_view()),
    path('find_similar_paper_titles', find_similar_paper_titles.as_view()),
    path('find_similar_news_titles', find_similar_news_titles.as_view()),
    path('find_similar_rumors_titles', find_similar_rumors_titles.as_view())

]
