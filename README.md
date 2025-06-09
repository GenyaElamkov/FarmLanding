# Лендинк

uv run src/manage.py runserver

uv run src/manage.py test src/tests/
uv run src/manage.py test tests.paperwork.models.test_document


pytest --cov=.
pytest --cov=. --cov-report=html
pytest --cov=. --cov-report=xml   # Генерирует отчёт в формате XML (например, для CI)
pytest --cov=. --cov-fail-under=80  # Завершится с ошибкой, если coverage < 80%