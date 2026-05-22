# RJ Bakery Backend

Django REST API for a bakery product catalogue with filtering, search, sorting, pagination, and star ratings.

RJ Bakery Backend is a Django REST API that powers a bakery product catalogue. It serves product data to a React frontend, enabling users to browse items by category, search, sort, paginate, and submit star ratings – all with secure image uploads and a custom admin panel. This is a portfolio project demonstrating full‑stack development with Django, PostgreSQL, Cloudinary, and Render.

## Live API
[https://rj-bakery-backend.onrender.com/api/products/](https://rj-bakery-backend.onrender.com/api/products/)

## Tech Stack
- Django & Django REST Framework
- PostgreSQL (Supabase) – optional, SQLite default
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

## Local Setup

### Prerequisites
- Python 3.12 or later
- pip and virtual environment
- Cloudinary account for image storage
- Supabase account for database (django's default database SQLite can also be used) 

### Installation

1. Clone the repository
   ```bash
   git clone git@github.com:sharu-19008/rj-bakery-backend.git
   cd rj-bakery-backend
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file (see Environment Variables section)

5. Run migrations
   ```bash
   python manage.py migrate
   ```

6. Create a superuser (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server
   ```bash
   python manage.py runserver
   ```

## Environment Variables

Create a `.env` file in the project root:

```env
# Django
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database – SQLite works out of the box (no extra setup)
DATABASE_URL=sqlite:///db.sqlite3

# For PostgreSQL (optional – uncomment and update if you prefer)
# DATABASE_URL=postgresql://postgres:password@localhost:5432/your_db_name

# Cloudinary (image storage – required for uploads)
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

# CORS (add your frontend URL)
CORS_ALLOWED_ORIGINS=http://localhost:5173,https://rj-bakery.netlify.app
```

> **Note:** Never commit your `.env` file. SQLite is the default – just copy `.env.example` to `.env` and run migrations. To switch to PostgreSQL, replace the `DATABASE_URL` value and comment out the SQLite line.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/products/` | List products (supports `category`, `search`, `sort`, `page`, `page_size`) |
| POST | `/api/products/<id>/rate/` | Submit a rating (1‑5) |

## Deployment

- Backend hosted on Render (free tier)
- Database on Supabase (free tier, PostgreSQL)
- Images stored on Cloudinary (free tier)
- Static files served via Whitenoise

## Frontend Repository

[https://github.com/sharu-19008/rj-bakery-frontend](https://github.com/sharu-19008/rj-bakery-frontend)

## License

MIT
