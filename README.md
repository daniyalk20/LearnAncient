# LearnAncient (MVP)

LearnAncient is a manuscript-centered ancient language learning
application. The stack consists of a Django REST backend and a
React/Vite PWA frontend.

The backend exposes a versioned REST API under `/api/v1/` that supports
authentication, language packs, passages, reader views, spaced
repetition reviews, and simple search.

## Backend quick start

```pwsh
cd backend
../.venv/Scripts/python.exe -m pip install -r ../requirements.txt
../.venv/Scripts/python.exe manage.py migrate
../.venv/Scripts/python.exe manage.py seed_biblical_greek
../.venv/Scripts/python.exe manage.py runserver
```

Key endpoints (all prefixed with `/api/v1/`):

- `POST /auth/login` – obtain JWT access/refresh pair
- `POST /auth/refresh` – refresh access token
- `POST /auth/guest-upgrade` – convert guest to account (MVP: creates user)
- `GET /languages` – list languages
- `GET /languages/{id}/packs` – list language packs
- `GET /passages/{id}` – passage with tokens
- `GET /reader/passage/{id}` – reader passage view
- `GET /reader/token/{id}` – token-level metadata
- `GET /search?q=` – basic global search
- `GET /review/due` – due review items (auth required)
- `POST /review/answer` – record review answer and reschedule

Further work includes richer SRS scheduling, advanced search,
and full language pack ingestion for Biblical Greek.

## Frontend quick start

```pwsh
cd frontend
npm install
npm run dev
```

The frontend runs at `http://localhost:5173` and proxies `/api` calls to
the Django backend.

The **Read** tab lets you explore the seeded Biblical Greek passage with
token-level interaction; the **Profile** and **Review** tabs demonstrate
authentication and SRS integration.
