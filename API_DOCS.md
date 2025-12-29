# Algeria Cities API Documentation

Complete API documentation for the Algeria Cities API.

## Base URL

**Production:**
```
https://algeria-cities.iyed.online/api
```

**Development:**
```
http://localhost:8000/api
```

## API Version

All endpoints are versioned under `/v1/`.

## Response Format

All API responses are in JSON format. The API uses Django REST Framework's JSON renderer.

## Endpoints

### 1. Get All Communes

Retrieve a list of all communes (cities) in Algeria.

**Endpoint:** `GET /api/v1/communes/`

**Response:** `200 OK`

```json
[
  {
    "num": 1,
    "commune_name": "Adrar",
    "commune_name_ascii": "Adrar",
    "daira_name": "Adrar",
    "daira_name_ascii": "Adrar",
    "wilaya_code": "1",
    "wilaya_name": "Adrar",
    "wilaya_name_ascii": "Adrar"
  },
  {
    "num": 2,
    "commune_name": "Tamest",
    "commune_name_ascii": "Tamest",
    "daira_name": "Adrar",
    "daira_name_ascii": "Adrar",
    "wilaya_code": "1",
    "wilaya_name": "Adrar",
    "wilaya_name_ascii": "Adrar"
  }
]
```

**Query Parameters:**

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `page` | integer | Page number for pagination | 1 |
| `page_size` | integer | Number of results per page | Varies |

**Example Request:**
```bash
# Production
curl https://algeria-cities.iyed.online/api/v1/communes/

# Development
curl http://localhost:8000/api/v1/communes/
```

---

### 2. Get All Wilayas

Retrieve a list of all wilayas (provinces) in Algeria, ordered by wilaya code.

**Endpoint:** `GET /api/v1/wilayas/`

**Response:** `200 OK`

```json
[
  {
    "wilaya_code": 1,
    "wilaya_name": "Adrar",
    "wilaya_name_ascii": "Adrar"
  },
  {
    "wilaya_code": 2,
    "wilaya_name": "Chlef",
    "wilaya_name_ascii": "Chlef"
  },
  {
    "wilaya_code": 3,
    "wilaya_name": "Laghouat",
    "wilaya_name_ascii": "Laghouat"
  }
]
```

**Example Request:**
```bash
# Production
curl https://algeria-cities.iyed.online/api/v1/wilayas/

# Development
curl http://localhost:8000/api/v1/wilayas/
```

---

### 3. Get Specific Wilaya

Retrieve details of a specific wilaya by its code.

**Endpoint:** `GET /api/v1/wilayas/<wilaya_code>/`

**Path Parameters:**

| Parameter | Type | Description | Valid Range |
|-----------|------|-------------|-------------|
| `wilaya_code` | integer | The wilaya code | 1-58 |

**Response:** `200 OK`

```json
{
  "wilaya_code": 16,
  "wilaya_name": "Alger",
  "wilaya_name_ascii": "Alger"
}
```

**Error Response:** `404 Not Found`

```json
{
  "detail": "Not found."
}
```

**Example Request:**
```bash
# Production
curl https://algeria-cities.iyed.online/api/v1/wilayas/16/

# Development
curl http://localhost:8000/api/v1/wilayas/16/
```

---

### 4. Get Communes by Wilaya

Retrieve all communes (cities) within a specific wilaya.

**Endpoint:** `GET /api/v1/wilayas/communes/<num>`

**Path Parameters:**

| Parameter | Type | Description | Valid Range |
|-----------|------|-------------|-------------|
| `num` | integer | The wilaya code | 1-58 |

**Response:** `200 OK`

```json
[
  {
    "num": 1,
    "commune_name": "Adrar",
    "commune_name_ascii": "Adrar",
    "daira_name": "Adrar",
    "daira_name_ascii": "Adrar",
    "wilaya_code": "1",
    "wilaya_name": "Adrar",
    "wilaya_name_ascii": "Adrar"
  },
  {
    "num": 2,
    "commune_name": "Tamest",
    "commune_name_ascii": "Tamest",
    "daira_name": "Adrar",
    "daira_name_ascii": "Adrar",
    "wilaya_code": "1",
    "wilaya_name": "Adrar",
    "wilaya_name_ascii": "Adrar"
  }
]
```

**Error Response:** `400 Bad Request`

If the wilaya code is out of range:

```json
{
  "error": "there is no wilaya with this number (1-58)"
}
```

**Example Request:**
```bash
# Production
curl https://algeria-cities.iyed.online/api/v1/wilayas/communes/16

# Development
curl http://localhost:8000/api/v1/wilayas/communes/16
```

---

## Data Models

### Commune Object

| Field | Type | Description |
|-------|------|-------------|
| `num` | integer | Unique commune number |
| `commune_name` | string | Commune name (may contain Arabic/French characters) |
| `commune_name_ascii` | string | Commune name in ASCII format |
| `daira_name` | string | District (daira) name |
| `daira_name_ascii` | string | District name in ASCII format |
| `wilaya_code` | string | Province code (1-58) |
| `wilaya_name` | string | Province name |
| `wilaya_name_ascii` | string | Province name in ASCII format |

### Wilaya Object

| Field | Type | Description |
|-------|------|-------------|
| `wilaya_code` | integer | Province code (1-58) |
| `wilaya_name` | string | Province name (may contain Arabic/French characters) |
| `wilaya_name_ascii` | string | Province name in ASCII format |

## Error Handling

The API uses standard HTTP status codes:

| Status Code | Description |
|-------------|-------------|
| `200` | Success |
| `400` | Bad Request - Invalid parameters |
| `404` | Not Found - Resource doesn't exist |
| `500` | Internal Server Error |

### Error Response Format

```json
{
  "error": "Error message description"
}
```

Or for DRF standard errors:

```json
{
  "detail": "Error message description"
}
```

## CORS

The API has CORS enabled for all origins. This allows cross-origin requests from web applications.

## Rate Limiting

Currently, there is no rate limiting implemented. Consider implementing rate limiting for production use.

## Pagination

The `/api/v1/communes/` endpoint supports pagination through Django REST Framework's default pagination. Use query parameters `page` and `page_size` to control pagination.

## Examples

### JavaScript (Fetch API)

```javascript
// Get all wilayas
fetch('https://algeria-cities.iyed.online/api/v1/wilayas/')
  .then(response => response.json())
  .then(data => console.log(data));

// Get communes in Algiers (wilaya code 16)
fetch('https://algeria-cities.iyed.online/api/v1/wilayas/communes/16')
  .then(response => response.json())
  .then(data => console.log(data));
```

### Python (requests)

```python
import requests

# Get all wilayas
response = requests.get('https://algeria-cities.iyed.online/api/v1/wilayas/')
wilayas = response.json()

# Get communes in Algiers
response = requests.get('https://algeria-cities.iyed.online/api/v1/wilayas/communes/16')
communes = response.json()
```

### cURL

```bash
# Production URLs
# Get all communes
curl https://algeria-cities.iyed.online/api/v1/communes/

# Get all wilayas
curl https://algeria-cities.iyed.online/api/v1/wilayas/

# Get specific wilaya
curl https://algeria-cities.iyed.online/api/v1/wilayas/16/

# Get communes by wilaya
curl https://algeria-cities.iyed.online/api/v1/wilayas/communes/16
```

## Notes

- All wilaya codes are integers between 1 and 58 (Algeria has 58 provinces)
- Commune names may contain Arabic characters, but ASCII versions are always provided
- The API returns data in JSON format only
- All endpoints are read-only (GET requests only)
- No authentication is required for accessing the API

## Support

For API issues or questions, please refer to the main [README.md](README.md) or open an issue in the repository.

