from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render


class AuthController:

    @staticmethod
    def signin(request):
        if request.method == 'POST':
            return AuthController.registration(request)

        return AuthController.create(request)

    @staticmethod
    def create(request):
        return render(request, 'auth/signin.html')

    @staticmethod
    def registration(request):
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

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

        if not password:
            errors['password'] = 'Поле пароль обязательно для заполнения.'
        elif len(password) < 6:
            errors['password'] = 'Пароль должен содержать минимум 6 символов.'

        if errors:
            return JsonResponse({
                'status': 'error',
                'message': 'Ошибка валидации данных.',
                'errors': errors
            }, status=422, json_dumps_params={'ensure_ascii': False})

        return JsonResponse({
            'status': 'success',
            'message': 'Регистрация успешно выполнена.',
            'data': {
                'name': name,
                'email': email,
                'password': password
            }
        }, json_dumps_params={'ensure_ascii': False})