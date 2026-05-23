# AgriManager Full Stack

A Django + Django REST Framework agriculture dashboard for:
- Sales data
- Purchase data
- Dispatch data
- Procurement quantity
- Farmer details
- Farmer payments
- Federation names

## Setup

1. Create a Python virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run migrations:

```powershell
python manage.py migrate
```

4. Start the development server:

```powershell
python manage.py runserver
```

5. Open the site:

`http://127.0.0.1:8000/`

## API endpoints

- `http://127.0.0.1:8000/api/sales/`
- `http://127.0.0.1:8000/api/purchases/`
- `http://127.0.0.1:8000/api/dispatches/`
- `http://127.0.0.1:8000/api/procurements/`
- `http://127.0.0.1:8000/api/farmers/`
- `http://127.0.0.1:8000/api/payments/`
- `http://127.0.0.1:8000/api/federations/`

<!-- ## Notes

- Use Django admin to add data or create API clients.
- Templates are in `core/templates/core`.
- Static CSS/JS are in `core/static/core`. -->
