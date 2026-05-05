# Weather Frontend Service

This service is the frontend microservice for the Weather App final project.

It provides a simple web UI that allows users to select a city and view live weather data.

---

## Features

- Dropdown with supported cities
- "Get Weather" button
- Displays:
  - Temperature
  - Description
  - Humidity
  - Wind speed
- Clean and simple UI
- Communicates with backend service

---

## Supported Cities

- New York
- Sydney
- Cape Town
- Bangkok

---

## How It Works
Browser → Frontend → Backend → OpenWeather API

- The browser sends a request to the frontend
- The frontend calls the backend service
- The backend fetches live weather data
- The frontend displays the result

---

## ⚙️ Environment Variables

| Variable | Description |
|----------|------------|
| BACKEND_URL | URL of the backend service |

### Example

```text
BACKEND_URL=http://localhost:5000


Run Locally
Install dependencies:
pip install -r requirements.txt
Set backend URL:
$env:BACKEND_URL="http://localhost:5000"
Run the app:
python app.py
Open in browser: http://localhost:5001


Run with Docker
Build the image: docker build -t weather-frontend .
Run the container: docker run -p 5001:5000 -e BACKEND_URL="http://host.docker.internal:5000" weather-frontend
Open in browser: http://localhost:5001

## Screenshot

![Weather Dashboard Screenshot](./screenshot.png)
<img width="1914" height="1033" alt="screenshot" src="https://github.com/user-attachments/assets/bcc4d4f8-afe9-4dad-a587-658060f96b55" />

Notes
The frontend runs inside the container on port 5000
It is exposed on port 5001 on the host to avoid conflict with the backend
The backend must be running before using the frontend
The backend URL is configurable via environment variable
