# 🔗 URL Shortener Backend

A backend for a URL shortener, built with **Python** and **Flask**.

The project is in its early stage. The Flask app, a health check API and a `POST /api/shorten` endpoint that receives a long URL are working and tested locally.

---

## 📅 Day 1 — Flask Setup & Health Check

### Completed

- Installed Flask
- Created the Flask application
- Created the home route
- Created the health check API
- Returned a JSON response
- Tested the backend locally

---

## 📅 Day 2 — REST API & POST Request

### Completed

- Learned GET and POST HTTP methods
- Learned how API requests work
- Learned JSON request bodies
- Created `POST /api/shorten`
- Used Flask `request.get_json()`
- Extracted URL from JSON data
- Added basic input validation
- Implemented HTTP 400 error response

---

## 🛠️ Technologies Used

- Python 3
- Flask

---

## ▶️ How to Run

### Step 1 — Install Flask

```bash
pip install flask
```

### Step 2 — Start the server

From the project folder, run:

```bash
python app.py
```

Flask starts a local development server, usually at `http://127.0.0.1:5000`.

> If your main file has a different name, replace `app.py` with it.

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check whether the backend is running |
| GET | `/api/health` | Check backend health |
| POST | `/api/shorten` | Receive a long URL |

### Example Health Response

```json
{
    "status": "success",
    "message": "Backend is healthy"
}
```

### Example Request — `POST /api/shorten`

```json
{
    "url": "https://www.example.com/this-is-a-long-url"
}
```

### Example Response

```json
{
    "status": "success",
    "message": "URL received successfully",
    "url": "https://www.example.com/this-is-a-long-url"
}
```

If the request has no URL, the API returns an **HTTP 400** error response.

---

## 🧪 Testing the Endpoints

Before moving forward, make sure all endpoints work.

### Endpoint 1 — Home

```text
GET /
```

Expected response:

```text
URL Shortener Backend is Running!
```

### Endpoint 2 — Health Check

```text
GET /api/health
```

Expected response:

```json
{
    "status": "success",
    "message": "Backend is healthy"
}
```

### Endpoint 3 — Shorten

```text
POST /api/shorten
```

Expected response:

```json
{
    "status": "success",
    "message": "URL received successfully",
    "url": "https://www.example.com/this-is-a-long-url"
}
```

You can test them from the terminal:

```bash
curl http://127.0.0.1:5000/
curl http://127.0.0.1:5000/api/health
curl -X POST http://127.0.0.1:5000/api/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.example.com/this-is-a-long-url"}'
```

---

## 🚀 Next Steps

- Generate a short code for each URL
- Store the original and short URLs
- Redirect short URLs to the original URL
- Improve validation and error handling