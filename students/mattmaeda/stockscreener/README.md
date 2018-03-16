# Stock Screener app

## Setup
1. In directory root, run `python -m venv venv`
2. Activate virtual environment `source venv/bin/activate`
3. Install required libraries `pip install -r requirements.txt`
4. Export Django application settings to environment `export DJANGO_SETTINGS_MODULE=stockscreener.settings`
5. Setup database `django-admin migrate`
6. Load initial rules and screen data `django-admin loaddata exchange/fixtures/initial_exchange_data.json`

## Run Application
1. `django-admin runserver`
2. Go to [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Run Tests
1. `django-admin test exchange
