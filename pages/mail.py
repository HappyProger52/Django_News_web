from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_article_created_email(article):
    subject = f'Добавлена новая статья: {article.title}'

    context = {
        'article': article,
        'site_name': settings.MAIL_FROM_NAME,
    }

    text_content = render_to_string(
        'emails/article_created.txt',
        context
    )

    html_content = render_to_string(
        'emails/article_created.html',
        context
    )

    message = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[settings.MODERATOR_EMAIL],
    )

    message.attach_alternative(html_content, 'text/html')
    message.send()