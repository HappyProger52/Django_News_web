from random import choice

from django.core.management.base import BaseCommand
from faker import Faker

from pages.models import Article


class Command(BaseCommand):
    help = 'Наполнение таблицы Article фейковыми данными'

    def handle(self, *args, **options):
        fake = Faker('ru_RU')

        preview_images = [
            'preview.jpg',
            'preview_2.jpg',
        ]

        full_images = [
            'full.jpeg',
            'full_2.jpeg',
        ]

        Article.objects.all().delete()

        for _ in range(10):
            Article.objects.create(
                title=fake.sentence(nb_words=6),
                short_description=fake.text(max_nb_chars=160),
                description=fake.text(max_nb_chars=800),
                preview_image=choice(preview_images),
                full_image=choice(full_images),
                published_at=fake.date_between(
                    start_date='-30d',
                    end_date='today'
                )
            )

        self.stdout.write(
            self.style.SUCCESS('Таблица Article успешно заполнена фейковыми данными.')
        )