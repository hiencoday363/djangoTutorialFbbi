### `py -m venv venv`
### `venv\Scripts\activate`
### `pip install -r requirements.txt`
## Config database
`py manage.py makemigrtations`

`py manage.py migrate`

`py manage.py runserver`


# For test
### `py manage.py makemigrations --dry-run (optional --verbosity 1,2,3)`
### `pip install coverage`
### `coverage run --omit='*../venv39/*' manage.py test`
### `coverage html`
