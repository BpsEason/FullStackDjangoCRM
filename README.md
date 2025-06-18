# FullStackDjangoCRM

A modern, full-stack Customer Relationship Management (CRM) system built with Django and Bootstrap 5, deployed using Docker. Designed for small to medium-sized businesses to manage customers, sales, activities, and reports, prioritizing security, performance, and scalability.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.1-green)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue)](https://www.docker.com/)
[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-blue)](https://github.com/BpsEason/FullStackDjangoCRM/actions)

## Overview
FullStackDjangoCRM is an open-source CRM system tailored for efficient customer relationship management. It offers a secure, scalable platform to track customers and activities, with plans for sales and reporting features. With a responsive Bootstrap 5 interface, Dockerized deployment, and internationalization (default: Traditional Chinese), it ensures ease of use for developers and businesses.

## Features
- **Customer Management**: Create, update, and track customer profiles with contact details, interaction history, and notes.
- **Activity Tracking**: Log and monitor calls, meetings, and tasks associated with customers.
- **Secure Authentication**: Role-based access control (RBAC) with Argon2 password hashing and CSRF/XSS protection.
- **Responsive UI**: Built with Bootstrap 5 for a mobile-friendly, modern interface.
- **Performance Optimized**: Redis caching and Celery for asynchronous tasks (e.g., email notifications).
- **Scalable Deployment**: Containerized with Docker and Docker Compose, ready for cloud or on-premises hosting.
- **Extensible**: REST API via Django REST Framework for future integrations.
- **Internationalization**: Supports multiple languages (default: zh-hant). Switch languages in `settings.py`.
- **Django Admin**: Powerful backend for managing customers and activities.
- **Planned Features**: Sales management (opportunities, quotes, orders) and reporting (sales funnel, customer analytics).

## Tech Stack
- **Backend**: Django 5.1, Django REST Framework 3.15
- **Frontend**: Bootstrap 5.3, Custom CSS/JS
- **Database**: PostgreSQL 16
- **Caching**: Redis 7
- **Task Queue**: Celery 5.4 with Redis backend
- **Deployment**: Docker, Docker Compose, Gunicorn 23, Nginx 1.25
- **Security**: Argon2 password hashing, `django-environ`, HSTS, secure cookies
- **Other Tools**: django-bootstrap5, psycopg2-binary

## Prerequisites
- Python 3.11+
- Docker and Docker Compose
- Git
- A code editor (e.g., VS Code)

## Installation (Local Development)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/BpsEason/FullStackDjangoCRM.git
   cd FullStackDjangoCRM
   ```

2. **Set up environment variables**:
   Copy the `.env.example` to `.env` and configure the values:
   ```bash
   cp .env.example .env
   ```
   Example `.env`:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DB_NAME=crm_db
   DB_USER=postgres
   DB_PASSWORD=postgres
   DB_HOST=db
   DB_PORT=5432
   REDIS_URL=redis://redis:6379/0
   CELERY_BROKER_URL=redis://redis:6379/0
   CELERY_RESULT_BACKEND=redis://redis:6379/0
   SECURE_SSL_REDIRECT=False
   SESSION_COOKIE_SECURE=False
   CSRF_COOKIE_SECURE=False
   ```

3. **Build and run with Docker Compose**:
   ```bash
   docker-compose up --build
   ```

4. **Apply database migrations**:
   ```bash
   docker-compose exec web python manage.py makemigrations
   docker-compose exec web python manage.py migrate
   ```

5. **Create a superuser**:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

6. **Collect static files**:
   ```bash
   docker-compose exec web python manage.py collectstatic --noinput
   ```

7. **Access the application**:
   - Web: `http://localhost`
   - Admin: `http://localhost/admin` (use superuser credentials)

## Deployment (Production)

1. **Configure production settings**:
   - Update `.env`:
     ```
     DEBUG=False
     ALLOWED_HOSTS=your-domain.com
     SECURE_SSL_REDIRECT=True
     SESSION_COOKIE_SECURE=True
     CSRF_COOKIE_SECURE=True
     ```
   - Generate a secure `SECRET_KEY`:
     ```bash
     python -c 'import secrets; print(secrets.token_hex(32))'
     ```

2. **Set up HTTPS**:
   - Use Let's Encrypt for SSL/TLS certificates.
   - Configure Nginx to enforce HTTPS and HSTS.

3. **Static files**:
   - Serve static files via a CDN (e.g., Cloudflare, AWS S3) for better performance.
   - Run `collectstatic` in production.

4. **Deploy to a cloud provider**:
   - Push Docker images to a registry (e.g., Docker Hub, AWS ECR).
   - Use AWS ECS, Google Cloud Run, or a VPS.
   - Example command:
     ```bash
     docker-compose -f docker-compose.prod.yml up --build
     ```

5. **Scaling**:
   - Use Kubernetes or Docker Swarm for orchestration.
   - Configure a load balancer (e.g., AWS ALB) for high availability.

6. **CI/CD**:
   - Set up GitHub Actions for automated testing and deployment. See `.github/workflows/ci.yml`.

## Project Structure
```
FullStackDjangoCRM/
├── crm/
│   ├── customers/           # Customer management app
│   ├── sales/              # Sales management app (planned)
│   ├── activities/         # Activity tracking app
│   ├── reports/            # Reporting app (planned)
│   ├── templates/          # HTML templates
│   ├── static/             # CSS, JS files
│   ├── settings.py         # Django settings
│   ├── urls.py             # URL routing
│   ├── wsgi.py             # WSGI configuration
├── docker/
│   ├── Dockerfile          # Docker configuration
│   ├── nginx.conf          # Nginx configuration
├── .env                    # Environment variables
├── docker-compose.yml      # Docker Compose configuration
├── requirements.txt        # Python dependencies
├── manage.py               # Django management script
├── LICENSE                 # MIT License
└── README.md               # This file
```

## Testing
Run unit tests to verify functionality:
```bash
docker-compose exec web python manage.py test
```
Tests cover customer and activity models. Contributions to expand test coverage are encouraged.

## Security Features
- **CSRF/XSS Protection**: Built-in Django middleware.
- **Password Hashing**: Argon2 for secure password storage.
- **HTTPS Enforcement**: Configurable HSTS and secure cookies.
- **Environment Variables**: Sensitive data stored in `.env` with `django-environ`.
- **RBAC**: Restricts data access to authorized users (e.g., creator-only data).

## Performance Optimizations
- **Caching**: Redis reduces database load with query caching.
- **Asynchronous Tasks**: Celery handles long-running tasks (e.g., email notifications).
- **Static Files**: Served via Nginx with Gzip compression, optional CDN support.
- **Database**: PostgreSQL with optimized Django ORM queries.

## Internationalization
- Default language: Traditional Chinese (`zh-hant`).
- To switch languages, update `LANGUAGE_CODE` in `crm/settings.py` (e.g., `en-us` for English).
- Run `django-admin compilemessages` after adding translations.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Follow PEP 8 for Python code and Bootstrap 5 conventions for templates.
4. Write unit tests for new features using Django's `TestCase`.
5. Commit your changes (`git commit -m 'Add your feature'`).
6. Push to the branch (`git push origin feature/your-feature`).
7. Open a Pull Request with a clear description and reference to related issues.

Please ensure your code passes tests and includes documentation.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or feedback, please:
- Open an issue on [GitHub](https://github.com/BpsEason/FullStackDjangoCRM/issues).
- Contact: [your-email@example.com](mailto:your-email@example.com).

## Acknowledgements
- Built with ❤️ using [Django](https://www.djangoproject.com/), [Bootstrap 5](https://getbootstrap.com/), and [Docker](https://www.docker.com/).
- Inspired by open-source CRM solutions and modern web development practices.

---

Happy managing your customers! 🚀