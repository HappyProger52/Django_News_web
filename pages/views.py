import json
from pathlib import Path

from django.http import Http404
from django.shortcuts import render


def load_news():
    json_path = Path(__file__).resolve().parent / 'static' / 'data' / 'news.json'

    with open(json_path, 'r', encoding='utf-8') as file:
        news = json.load(file)

    for index, item in enumerate(news):
        item['id'] = index
        item['preview_path'] = 'images/' + item['preview_image']
        item['full_path'] = 'images/' + item['full_image']

        if 'shortDesc' not in item:
            item['shortDesc'] = item['desc'][:150] + '...'

    return news


def home(request):
    news = load_news()

    return render(request, 'pages/home.html', {
        'news': news
    })


def galery(request, news_id):
    news = load_news()

    if news_id < 0 or news_id >= len(news):
        raise Http404('Новость не найдена')

    article = news[news_id]

    return render(request, 'pages/galery.html', {
        'article': article
    })


def about(request):
    return render(request, 'pages/about.html')


def contacts(request):
    contacts_data = [
        {
            'title': 'Редакция',
            'value': 'news@example.com',
            'description': 'Пишите нам по вопросам новостей и публикаций.'
        },
        {
            'title': 'Телефон',
            'value': '+7 (777) 123-45-67',
            'description': 'Звонки принимаются с 9:00 до 18:00.'
        },
        {
            'title': 'Адрес',
            'value': 'г. Алматы, ул. Абая, 10',
            'description': 'Главный офис новостного портала.'
        },
        {
            'title': 'Социальные сети',
            'value': '@news_portal',
            'description': 'Следите за нами в социальных сетях.'
        },
    ]

    return render(request, 'pages/contacts.html', {
        'contacts': contacts_data
    })