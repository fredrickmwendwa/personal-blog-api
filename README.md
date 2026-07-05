# Personal Blog API

A RESTful API for a personal blog, built with Django and Django REST Framework. Supports user authentication and full CRUD operations on blog posts, with ownership-based permissions.

## Features

- User signup, login, and logout using token-based authentication
- User profiles (bio, profile picture) automatically created on signup
- Full CRUD for blog posts (create, read, update, delete)
- Public read access to posts; write access restricted to authenticated users
- Ownership enforcement — only a post's author can update or delete it
- PostgreSQL database

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Token Authentication (DRF built-in)

## Project Structure

```
personal_blog_api/
├── config/       # Project settings and root URL config
├── accounts/           # User auth, profiles
├── posts/               # Blog posts CRUD
├── requirements.txt
└── manage.py
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/fredrickmwendwa/personal-blog-api.git
cd personal-blog-api
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up PostgreSQL

Create a database:

```sql
CREATE DATABASE blog_api_db;
```

### 5. Create a `.env` file in the project root

```
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=blog_api_db
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
```

### 6. Run migrations

```bash
python manage.py migrate
```

### 7. Create a superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 8. Run the server

```bash
python manage.py runserver
```

API will be available at `http://127.0.0.1:8000/`

## API Endpoints

### Auth

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| POST | `/api/auth/signup/` | Register a new user | No |
| POST | `/api/auth/login/` | Log in and receive a token | No |
| POST | `/api/auth/logout/` | Log out (deletes token) | Yes |

### Profile

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| GET | `/api/auth/profile/` | View your own profile | Yes |
| PATCH | `/api/auth/profile/update/` | Update your own profile | Yes |

### Posts

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| GET | `/api/posts/` | List all posts | No |
| POST | `/api/posts/` | Create a new post | Yes |
| GET | `/api/posts/<id>/` | View a single post | No |
| PATCH/PUT | `/api/posts/<id>/` | Update a post (owner only) | Yes |
| DELETE | `/api/posts/<id>/` | Delete a post (owner only) | Yes |

## Authentication

All authenticated requests must include this header:

```
Authorization: Token <your_token_here>
```

The token is returned in the response body when you sign up or log in.

## Testing

A Postman collection and environment are included in the repo:

- `Personal_Blog_API.postman_collection.json`
- `Blog_API_Local.postman_environment.json`

Import both into Postman to run the full test suite.