# Docker Setup Guide

This project includes Docker Compose configuration to run both the frontend and backend services together.

## Prerequisites

- Docker Desktop (or Docker Engine + Docker Compose)
- At least 2GB of available RAM

## Quick Start

1. **Create environment file** (optional, for custom configuration):
   ```bash
   cp .env.example .env
   # Edit .env with your settings if needed
   ```

2. **Build and start services**:
   ```bash
   docker-compose up --build
   ```

3. **Access the applications**:
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000/api
   - Django Admin: http://localhost:8000/admin

## Services

### Backend (Django)
- **Port**: 8000
- **Container**: `mmd-todo-backend`
- **API Endpoint**: `/api/todo/`
- **Database**: SQLite (persisted in Docker volume)

### Frontend (SvelteKit)
- **Port**: 5173
- **Container**: `mmd-todo-frontend`
- **Hot Reload**: Enabled in development mode

## Development Features

- **Hot Reload**: Both frontend and backend support hot-reload
- **Volume Mounting**: Code changes are reflected immediately
- **Health Checks**: Services wait for dependencies to be healthy
- **Persistent Data**: Database and media files are stored in Docker volumes

## Common Commands

### Start services
```bash
docker-compose up
```

### Start in detached mode
```bash
docker-compose up -d
```

### Stop services
```bash
docker-compose down
```

### View logs
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f backend
docker-compose logs -f frontend
```

### Rebuild after dependency changes
```bash
docker-compose up --build
```

### Run Django management commands
```bash
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py collectstatic
```

### Access shell
```bash
# Backend shell
docker-compose exec backend bash

# Frontend shell
docker-compose exec frontend sh
```

### Clean up (removes volumes)
```bash
docker-compose down -v
```

## Production Build

To build for production, modify `docker-compose.yml`:

1. Change build targets:
   ```yaml
   backend:
     build:
       target: production
   
   frontend:
     build:
       target: production
   ```

2. Update environment variables in `.env`:
   - Set `DEBUG=0`
   - Set a secure `SECRET_KEY`
   - Configure `ALLOWED_HOSTS`

3. Build and run:
   ```bash
   docker-compose -f docker-compose.yml up --build
   ```

## Volumes

- `backend_db`: SQLite database persistence
- `backend_media`: User-uploaded media files
- `backend_static`: Collected static files

## Networking

Both services are on the `mmd-todo-network` bridge network and can communicate using service names:
- Frontend can reach backend at: `http://backend:8000`
- Browser accesses backend at: `http://localhost:8000`

## Troubleshooting

### Port already in use
If ports 8000 or 5173 are already in use, modify the port mappings in `docker-compose.yml`:
```yaml
ports:
  - "8001:8000"  # Change host port
```

### Database migration errors
```bash
docker-compose exec backend python manage.py migrate
```

### Permission issues
On Linux, you may need to fix permissions:
```bash
sudo chown -R $USER:$USER backend/media backend/static
```

### Clear everything and start fresh
```bash
docker-compose down -v
docker-compose up --build
```

## Environment Variables

Key environment variables (set in `.env` file):

- `DEBUG`: Django debug mode (1 for dev, 0 for production)
- `SECRET_KEY`: Django secret key
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `VITE_API_URL`: Backend API URL for frontend

## Notes

- The database file (`db.sqlite3`) is stored in a Docker volume and persists between container restarts
- Media files uploaded through the Django admin or API are stored in the `backend_media` volume
- Static files are collected automatically on container start
- Health checks ensure services start in the correct order

