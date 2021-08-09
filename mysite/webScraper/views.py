from django.http.response import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import News

# Create your views here.

# @api_view()
def scrape(request):
    news = requests.get('https://www.thetitlereport.com/Articles.aspx?taxonomy=industrynews')
    soup = BeautifulSoup(news.text, 'html.parser')
    headings = soup.findAll("a", attrs={'class': 'ArticleLinks'})
    desc = soup.findAll("div", attrs={'class': 'Story_Page_Body'})
    # for heading in headings:
    #     News.objects.create(title=heading.text)

    news_dict = {}

    for key in headings:
        for value in desc:
            news_dict[key.text] = value.text
            desc.remove(value)
            break

    for key, value in news_dict.items():
        News.objects.create(title=key, desc=value)

    news_list = News.objects.all() 

    return render(request, 'home.html', {'news_list': news_list})


