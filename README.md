# FastAPI Learning Project

A hands-on project for learning FastAPI - the modern, fast, and high-performance Python web framework.

## Features of FastAPI

- **High Performance** - One of the fastest Python frameworks, on par with NodeJS and Go
- **Automatic API Documentation** - Interactive docs with Swagger UI and ReDoc out of the box
- **Type Hints** - Full editor support with autocompletion and type checking
- **Data Validation** - Automatic request validation using Pydantic
- **Async Support** - Native support for async/await syntax
- **Standards Based** - Built on OpenAPI and JSON Schema standards
- **Dependency Injection** - Powerful and easy-to-use DI system
- **Security** - Built-in support for OAuth2, JWT tokens, and more

## 📁 Production-Ready Directory Structure

```
fastapi-app/
├── app/
│   ├── main.py                # App entry point
│   │
│   ├── core/                  # Core application config
│   │   ├── config.py          # Settings (env-based)
│   │   ├── security.py        # Auth, JWT, hashing
│   │   ├── logging.py         # Logging setup
│   │
│   ├── api/                   # API layer
│   │   ├── __init__.py
│   │   ├── deps.py            # Dependencies (DB, auth)
│   │   │
│   │   └── v1/                # API versioning
│   │       ├── __init__.py
│   │       ├── router.py      # Combines all routes
│   │       ├── users.py       # User endpoints
│   │       └── auth.py        # Auth endpoints
│   │
│   ├── models/                # Database models
│   │   ├── __init__.py
│   │   └── user.py
│   │
│   ├── schemas/               # Pydantic schemas
│   │   ├── __init__.py
│   │   └── user.py
│   │
│   ├── services/              # Business logic
│   │   └── user_service.py
│   │
│   ├── db/                    # Database setup
│   │   ├── base.py            # Base model
│   │   ├── session.py         # Session / engine
│   │   └── migrations/        # Alembic
│   │
│   ├── utils/                 # Helpers
│   │   └── email.py
│   │
│   └── tests/
│       └── test_users.py
│
├── pyproject.toml
├── uv.lock
├── Dockerfile
├── .env
└── README.md

```

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd FastAPIProject
   ```

2. **Install uv** (if not already installed)
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Create virtual environment and install dependencies**
   ```bash
   uv sync
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

### Running the Application

**Development mode with auto-reload:**
```bash
uv run uvicorn main:app --reload
```

**Or using FastAPI CLI:**
```bash
uv run fastapi dev main.py
```

**Production mode:**
```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8000
```

### Adding Dependencies

```bash
# Add a new package
uv add <package-name>

# Add a dev dependency
uv add --dev <package-name>

# Remove a package
uv remove <package-name>
```

## API Documentation

Once the server is running, access the interactive documentation:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Running Tests

```bash
uv run pytest
```

## Learning Resources

- [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Starlette Documentation](https://www.starlette.io/)

## 📝 License

This project is for learning purposes.