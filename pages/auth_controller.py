from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.middleware.csrf import rotate_token
from django.shortcuts import redirect, render

from .models import Role, UserRole


class AuthController:

    @staticmethod
    def register_form(request):
        return render(request, 'auth/register.html')

    @staticmethod
    def register(request):
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        password_confirm = request.POST.get('password_confirm', '').strip()

        errors = {}

        if not name:
            errors['name'] = 'Поле имя обязательно для заполнения.'
        elif len(name) < 2:
            errors['name'] = 'Имя должно содержать минимум 2 символа.'

        if not email:
            errors['email'] = 'Поле email обязательно для заполнения.'
        else:
            try:
                validate_email(email)
            except ValidationError:
                errors['email'] = 'Введите корректный email.'

            if User.objects.filter(email=email).exists():
                errors['email'] = 'Пользователь с таким email уже существует.'

        if not password:
            errors['password'] = 'Поле пароль обязательно для заполнения.'
        elif len(password) < 6:
            errors['password'] = 'Пароль должен содержать минимум 6 символов.'

        if password != password_confirm:
            errors['password_confirm'] = 'Пароли не совпадают.'

        if errors:
            return render(request, 'auth/register.html', {
                'errors': errors,
                'old': {
                    'name': name,
                    'email': email,
                }
            })

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name
        )

        user.save()

        reader_role, _ = Role.objects.get_or_create(
            code='reader',
            defaults={
                'name': 'Читатель'
            }
        )

        UserRole.objects.create(
            user=user,
            role=reader_role
        )

        return redirect('login')

    @staticmethod
    def login_form(request):
        return render(request, 'auth/login.html')

    @staticmethod
    def login_user(request):
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        errors = {}

        if not email:
            errors['email'] = 'Поле email обязательно для заполнения.'

        if not password:
            errors['password'] = 'Поле пароль обязательно для заполнения.'

        if errors:
            return render(request, 'auth/login.html', {
                'errors': errors,
                'old': {
                    'email': email
                }
            })

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is None:
            errors['auth'] = 'Неверный email или пароль.'

            return render(request, 'auth/login.html', {
                'errors': errors,
                'old': {
                    'email': email
                }
            })

        login(request, user)

        return redirect('home')

    @staticmethod
    def logout_user(request):
        logout(request)
        rotate_token(request)

        return redirect('home')