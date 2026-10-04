# 🔗 URL Shortener Backend

A backend for a URL shortener, built with **Python** and **Flask**.

The project is in its early stage. The Flask app, a home route and a health check API are working and tested locally.

---

## ✅ Progress So Far

- Installed Flask
- Created the Flask application
- Created the home route
- Created the health check API
- Returned a JSON response
- Tested the backend locally

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

### Example Health Response

```json
{
    "status": "success",
    "message": "Backend is healthy"
}
```

---

## 🧪 Testing the Endpoints

Before moving forward, make sure both endpoints work.

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

You can test them in the browser or from the terminal:

```bash
curl http://127.0.0.1:5000/
curl http://127.0.0.1:5000/api/health
```

---

## 🚀 Next Steps

- Create an endpoint that accepts a long URL
- Generate a short code for each URL
- Store the original and short URLs
- Redirect short URLs to the original URL
- Add validation and error handling