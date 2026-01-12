# Moments: Mind Studio - Backend API

## Prerequisites

- **Python 3.12+**
- **uv** (Python package manager): https://docs.astral.sh/uv/

Install uv:
```bash
# macOS
brew install uv

# Or via pip
pip install uv
```

## Development Setup

```bash
cd apps/backend

# Create virtual environment with Python 3.12
uv venv --python 3.12

# Activate virtual environment
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

# Install dependencies
uv pip install -e ".[dev]"

# Install AI dependencies (optional, for Playwright archiving)
uv pip install -e ".[dev,ai]"

# Install Playwright browsers
playwright install chromium
```

## Running the Server

```bash
# Development server with hot reload
uvicorn app.main:app --reload --port 8000

# Production
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API Documentation

Once running, access:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/` | Root endpoint |
| `GET` | `/api/v1/health` | Health check |
| `POST` | `/api/v1/capture` | Capture a URL (2-second target) |
| `POST` | `/api/v1/archive` | Archive a captured page |
| `GET` | `/api/v1/benchmark` | Run 10-site benchmark |
| `GET` | `/api/v1/benchmark/summary` | Get Go/No-Go decision |

## Environment Variables

Create a `.env` file:

```bash
cp .env.example .env
```

Required variables:
```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
R2_ENDPOINT=https://your-account-id.r2.cloudflarestorage.com
R2_ACCESS_KEY=your-access-key
R2_SECRET_KEY=your-secret-key
R2_BUCKET=moments-archives
```

## Testing

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test
pytest tests/test_api.py -v
```

## Linting & Formatting

```bash
# Lint with ruff
ruff check app/

# Format with ruff
ruff format app/

# Type check with mypy
mypy app/
```

## Dependency Management

```bash
# Add a new dependency: edit pyproject.toml, then:
uv pip install -e "."

# Generate lock file for reproducible builds
uv pip compile pyproject.toml -o requirements.lock

# Install from lock file (CI/CD)
uv pip sync requirements.lock
```
