from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html')


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
            'value': '+7 (777) 000 00 01',
            'description': 'Звонки принимаются с 9:00 до 18:00.'
        },
        {
            'title': 'Адрес',
            'value': 'г Рязань ул Пушкина д 10',
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