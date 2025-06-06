uv run src/manage.py runserver_plus --cert-file cert.pem
uv run src/manage.py runserver 

uv run src/manage.py test src/tests/
uv run src/manage.py test tests.paperwork.models.test_document


coverage run manage.py test
coverage report
coverage html