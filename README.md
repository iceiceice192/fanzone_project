
# FanZone — Django Lab Project

Веб-приложение для спортивных фанатов с настройкой любимых команд и пользовательскими настройками, сохраняемыми в cookies.

## Структура проекта
- `fanzone/` — Django-проект
- `teams/` — Django-приложение с логикой выбора любимых команд
- `static/` — статические файлы (CSS, изображения)
- `templates/` — HTML-шаблоны

## Установка и запуск (локально)
1. Клонируйте репозиторий (или распакуйте архив).
2. Создайте виртуальное окружение и активируйте его:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Перейдите в папку проекта и выполните миграции:
   ```bash
   cd fanzone_project/fanzone
   python manage.py migrate
   ```
   *(Проект использует данные, заданные прямо в коде — моделей не требуется.)*
5. Запустите сервер разработки:
   ```bash
   python manage.py runserver
   ```
6. Откройте в браузере: http://127.0.0.1:8000/

## Git / GitHub
Пример команд для инициализации репозитория и загрузки на GitHub:
```bash
git init
git add .
git commit -m "Initial commit — FanZone lab project"
# создайте репозиторий на GitHub и затем:
git remote add origin https://github.com/USERNAME/REPO.git
git branch -M main
git push -u origin main
```

## Что реализовано
- HTML-форма для выбора любимых команд, темы (light/dark) и языка интерфейса.
- Стили оформлены через внешний CSS (static/css/styles.css).
- Сохранение пользовательских настроек через cookies: favorites (список команд), theme, lang, last_pages.
- Шаблоны: базовый шаблон, страница выбора и страница отображения сохранённых избранных команд.
- Инструкции по тестированию и дальнейшему улучшению в комментариях к коду.

