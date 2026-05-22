# RJ Bakery Backend

Django REST API for a bakery product catalogue with filtering, search, sorting, pagination, and star ratings.

RJ Bakery Backend is a Django REST API that powers a bakery product catalogue. It serves product data to a React frontend, enabling users to browse items by category, search, sort, paginate, and submit star ratings – all with secure image uploads and a custom admin panel. This is a portfolio project demonstrating full‑stack development with Django, PostgreSQL, Cloudinary, and Render.

## Live API
`https://rj-bakery-backend.onrender.com/api/products/`

## Tech Stack
- Django & Django REST Framework
- PostgreSQL (Supabase)
- Cloudinary (image storage)
- Gunicorn (production server)
- Deployed on Render

## Features
- Product CRUD via admin panel
- Category filtering (`?category=breads-and-buns`)
- Search (`?search=chocolate`)
- Sorting (`?sort=price_low`, `name_asc`, `rating_desc`, etc.)
- Pagination (`?page=2&page_size=12`)
- Star rating endpoint (`POST /api/products/<id>/rate/`)
- Rate limiting (50 requests/minute per IP)
- Custom admin URL for security
- CORS configured for frontend

## Installation and Local Setup
1. Clone the repo
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Create `.env` file (see `.env.example` for required variables)
6. Run migrations: `python manage.py migrate`
7. Create superuser: `python manage.py createsuperuser`
8. Run server: `python manage.py runserver`

## Required Environment Variables (`.env.example`)
DJANGO_SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgresql://... (your postgresql conntection string)
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
CORS_ALLOWED_ORIGINS=http://localhost:5173,https://rj-bakery.netlify.app

## Deployment
- Backend hosted on Render (free tier)
- Database on Supabase (free tier, PostgreSQL)
- Images stored on Cloudinary (free tier)
- Static files served via Whitenoise

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/products/` | List products (with filters, search, sort, pagination) |
| POST | `/api/products/<id>/rate/` | Submit a rating (1‑5) |

## License
MIT

