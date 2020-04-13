
# pysample
Python Django testing project for play around with features.

Current active working branch is `master`.

### How to Run:
- Requires Python 3.7, Django
- Checkout the project
- Navigate to project root, issue command:
    - On macOS: `python3 manage.py runserver`
    - On windows and linux:  `python manage.py runserver`

- Navigate to: http://127.0.0.1:8000/blog/ or http://127.0.0.1:8000/admin/

### SQLite DB Setup:
- Install Sqlite Browser from https://sqlitebrowser.org/dl/
```
python3 manage.py makemigrations
python3 manage.py migrate
```

### Create Admin User:
- `python3 manage.py createsuperuser`




