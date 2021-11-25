py -m venv venv
venv\Scripts\activate
pip install django
django-admin startproject core .
py manage.py startapp users
py manage.py makemigrations --dry-run (optional --verbosity 1,2,3)
pip install coverage
coverage run --omit='*../venv39/*' manage.py test
coverage html
