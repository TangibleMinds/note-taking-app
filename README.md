# Note Taking App

A FastAPI-based note-taking application with a PostgreSQL backend, web UI using Jinja2 templates and Bootstrap, and deployment on Vercel.

## Features

- Create, Read, Update, Delete (CRUD) notes
- RESTful API with FastAPI
- PostgreSQL database using SQLAlchemy
- Web UI with Jinja2 and Bootstrap
- Unit tests with Pytest
- Continuous Integration with GitHub Actions
- Code linting and formatting with pre-commit hooks
- Deployable on Vercel

## Setup

### Prerequisites

- Python 3.11+
- PostgreSQL
- Poetry

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/note-taking-app.git
   cd note-taking-app
   ```

2. **Install dependencies:**

   ```bash
   poetry install
   ```
3. **Install Postgres Client (Instructions for Ubuntu) (Optional):**

   ```bash
   sudo apt install postgresql
   sudo apt install postgresql-client-common
   sudo apt-get install -y postgresql-client

   sudo systemctl restart postgresql # start the server

   # Need to make sure we have the correct user and password
   sudo -u postgres psql

   \conninfo # this should give you the username, database name and port number, we create a new database for this app

   \password postgres # this is to change the password for the default user - postgres

   CREATE DATABASE note_db; # this is to create the database

   \q # use this to quit from the psql cli
   ```

4. **Set up the database:**

   Ensure PostgreSQL is running and create a database:

   ```bash
   createdb note_db
   ```

   Update the `DATABASE_URL` in `app/database.py` if necessary.

5. **Run database migrations:**

   The models are set to create tables automatically on startup.

6. **Start the application:**

   ```bash
   poetry run uvicorn app.main:app --port 3000 --reload # you can see this running in localhost:3000
   ```

7. **Access the application:**

   Open [http://localhost:8000](http://localhost:8000) in your browser. # this is the default port

## Testing

Run the tests using:

```bash
poetry run pytest
```

## Deployment

The application is configured to deploy on Vercel. Ensure you set the `DATABASE_URL` environment variable in Vercel settings.

## License

MIT License
```

---

## Summary of All Files

1. **`pyproject.toml`** - Poetry dependency and project configuration.
2. **`.pre-commit-config.yaml`** - Pre-commit hooks setup.
3. **`.github/workflows/ci.yml`** - GitHub Actions CI workflow.
4. **`vercel.json`** - Vercel deployment configuration.
5. **`app/main.py`** - FastAPI application entry point.
6. **`app/models.py`** - SQLAlchemy models.
7. **`app/schemas.py`** - Pydantic schemas.
8. **`app/crud.py`** - CRUD operations.
9. **`app/database.py`** - Database connection setup.
10. **`app/api/notes.py`** - API routes for notes.
11. **`app/templates/base.html`** - Base HTML template.
12. **`app/templates/index.html`** - Main page template.
13. **`static/css/styles.css`** - Custom CSS.
14. **`static/js/scripts.js`** - JavaScript for frontend interactions.
15. **`tests/test_notes.py`** - Unit tests for the API.
16. **`README.md`** - Project documentation.

---

## Next Steps

1. **Initialize Git Repository:**

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Set Up GitHub Repository:**

   ```bash
   git remote add origin https://github.com/yourusername/note-taking-app.git
   git push -u origin main
   ```

3. **Configure Vercel Deployment:**

   - Connect your GitHub repository to Vercel.
   - Set the `DATABASE_URL` environment variable in Vercel.
   - Deploy the application.

4. **Run Pre-commit Hooks:**

   ```bash
   poetry run pre-commit install
   ```

Now, your FastAPI note-taking application is set up with best practices for development, testing, and deployment!
