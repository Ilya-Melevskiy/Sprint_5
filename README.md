# Sprint_5
# Проект автоматизации тестирования учебного сервиса "Доска"
1. Основа для написания автотестов — фреймворк pytest.
2. Установить зависимости — pip install -r requirements.txt.
3. Команда для запуска — pytest -v.

Реализованы тесты:

-Регистрация пользователя: test_registration_user_success
-Регистрация пользователя c email не по маске  *******@*******.***: test_registration_user_invalid_email_error
-Регистрация уже существующего пользователя: test_registration_existing_user__error

-Login пользователя: test_login_user_success

-Logout пользователя: test_logout_user_success

-Создание объявления неавторизованным пользователем: test_unauth_user_place_announcement
-Создание объявления авторизованным пользователем: test_auth_user_place_announcement