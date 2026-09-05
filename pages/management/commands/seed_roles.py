from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from pages.models import Role, UserRole


class Command(BaseCommand):
    help = 'Создание ролей и пользователя-модератора'

    def handle(self, *args, **options):
        moderator_role, _ = Role.objects.get_or_create(
            code='moderator',
            defaults={
                'name': 'Модератор'
            }
        )

        reader_role, _ = Role.objects.get_or_create(
            code='reader',
            defaults={
                'name': 'Читатель'
            }
        )

        moderator, created = User.objects.get_or_create(
            username='moderator@test.ru',
            defaults={
                'email': 'moderator@test.ru',
                'first_name': 'Модератор'
            }
        )

        if created:
            moderator.set_password('123456')
            moderator.save()

        UserRole.objects.update_or_create(
            user=moderator,
            defaults={
                'role': moderator_role
            }
        )

        self.stdout.write(
            self.style.SUCCESS(
                'Роли созданы. Пользователь-модератор создан: moderator@test.ru / 123456'
            )
        )