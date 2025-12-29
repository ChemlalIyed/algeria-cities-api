# Algeria Cities API

A RESTful API built with Django and Django REST Framework that provides access to comprehensive data about cities (communes), districts (dairas), and provinces (wilayas) in Algeria.

**🌐 Live API:** [https://algeria-cities.iyed.online](https://algeria-cities.iyed.online)

## Features

- 🏙️ Complete database of all Algerian communes (cities)
- 🗺️ Information about all 58 wilayas (provinces) in Algeria
- 📍 District (daira) information for each commune
- 🌐 RESTful API endpoints with JSON responses
- 🔓 CORS enabled for cross-origin requests
- 📊 Well-structured data models

## Tech Stack

- **Django** 5.2.4
- **Django REST Framework** 3.16.0
- **PostgreSQL** (via psycopg2)
- **django-cors-headers** for CORS support
- **python-dotenv** for environment variable management

## Project Structure

```
algeria_cities_api/
├── algeria_cities_api/     # Main project directory
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   └── views.py            # Root views
├── api/                     # API application
│   ├── models.py           # Data models (Algeria_cities, Algeria_Wilaya)
│   ├── views.py            # API view classes
│   ├── serializer.py       # DRF serializers
│   └── urls.py             # API URL routing
├── template/                # HTML templates
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies
```

## Installation

### Prerequisites

- Python 3.8 or higher
- PostgreSQL database
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd algeria_cities_api
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   
   Create a `.env` file in the project root with the following variables:
   ```env
   SECRET_KEY=your-secret-key-here
   db_url=postgresql://user:password@host:port/database?sslmode=require
   ```

6. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

7. **Load initial data** (if you have a SQL file)
   ```bash
   python manage.py loaddata api/db.sql
   ```
   Or import your database dump directly to PostgreSQL.

8. **Create a superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

9. **Run the development server**
   ```bash
   python manage.py runserver
   ```

   The API will be available at `http://localhost:8000`

## API Documentation

For detailed API documentation, see [API_DOCS.md](API_DOCS.md)

### Quick Start

**Production API Base URL:** `https://algeria-cities.iyed.online/api`

- **Get all communes**: `GET https://algeria-cities.iyed.online/api/v1/communes/`
- **Get all wilayas**: `GET https://algeria-cities.iyed.online/api/v1/wilayas/`
- **Get communes by wilaya**: `GET https://algeria-cities.iyed.online/api/v1/wilayas/communes/<wilaya_code>`
- **Get specific wilaya**: `GET https://algeria-cities.iyed.online/api/v1/wilayas/<wilaya_code>/`

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SECRET_KEY` | Django secret key for cryptographic signing | Yes |
| `db_url` | PostgreSQL database connection URL | Yes |

## Configuration

- **DEBUG**: Set to `False` in production
- **ALLOWED_HOSTS**: Currently set to `['*']` - restrict this in production
- **CORS**: Enabled for all origins - configure appropriately for production

## Database Models

### Algeria_cities
Represents a commune (city) in Algeria with the following fields:
- `num`: Commune number
- `commune_name`: Commune name (Arabic/French)
- `commune_name_ascii`: Commune name in ASCII
- `daira_name`: District name
- `daira_name_ascii`: District name in ASCII
- `wilaya_code`: Province code (1-58)
- `wilaya_name`: Province name
- `wilaya_name_ascii`: Province name in ASCII

### Algeria_Wilaya
Represents a wilaya (province) in Algeria with the following fields:
- `wilaya_code`: Province code (1-58)
- `wilaya_name`: Province name
- `wilaya_name_ascii`: Province name in ASCII

## Development

### Running Tests
```bash
python manage.py test
```

### Accessing Admin Panel
Navigate to `http://localhost:8000/admin/` and log in with your superuser credentials.

## Production Deployment

1. Set `DEBUG = False` in `settings.py`
2. Configure `ALLOWED_HOSTS` with your domain
3. Set up proper CORS configuration
4. Use a production-grade WSGI server (e.g., Gunicorn)
5. Set up proper database connection pooling
6. Configure static files serving
7. Use environment variables for sensitive data

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or contributions, please open an issue on the repository.

## Acknowledgments

- Data sourced from official Algerian administrative divisions
- Built with Django and Django REST Framework
