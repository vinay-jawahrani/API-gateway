# API Gateway with Service Aggregation

[![GitHub](https://img.shields.io/badge/GitHub-Repo-black)](https://github.com/vinay-jawahrani/API-gateway)
[![Live Demo](https://img.shields.io/badge/Live_Demo-View_App-blue)](https://api-gateway-nine-theta.vercel.app/)
[![Backend](https://img.shields.io/badge/Backend-API-green)](https://api-gateway-masj.onrender.com/docs)

A full-stack API Gateway that aggregates Weather, News, and Quotes APIs into a single dashboard with Redis caching and Circuit Breaker pattern.

---

## 🚀 Features

- **Service Aggregation** – Fetch Weather, News, and Quotes in one unified dashboard
- **Redis Caching** – 5-minute TTL caching to reduce external API calls
- **Circuit Breaker Pattern** – Prevents cascading failures when external services are down
- **Async Parallel Requests** – `asyncio.gather()` for faster response times
- **Interactive Dashboard** – React-based UI with real-time updates
- **Source Tracking** – Know whether data comes from cache or live API
- **Auto-generated Docs** – Swagger UI at `/docs`
- **Containerized** – Docker support for consistent deployment

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend Framework** | FastAPI (Python) |
| **Frontend Framework** | Next.js 15 (React) |
| **Caching** | Redis (Upstash) |
| **HTTP Client** | httpx (async) |
| **API Calls** | Axios |
| **Deployment** | Render (Backend) + Vercel (Frontend) |
| **Containerization** | Docker (optional) |

---

## 📌 API Endpoints

| Method | Endpoint | Description | Cached |
|--------|----------|-------------|--------|
| GET | `/` | Welcome message | ❌ |
| GET | `/health` | Health check + Redis status | ❌ |
| GET | `/weather?city=London` | Get weather data for a city | ✅ (5 min) |
| GET | `/news?limit=3` | Get top news headlines | ✅ (5 min) |
| GET | `/quotes` | Get a random quote | ✅ (5 min) |
| GET | `/dashboard` | Aggregate all services in one call | ❌ |

---

## 📁 Project Structure
API-gateway/
├── backend/
│ ├── app/
│ │ ├── init.py
│ │ ├── main.py # FastAPI application
│ │ ├── services.py # External API calls
│ │ └── cache.py # Redis caching logic
│ ├── venv/ # Virtual environment (ignored)
│ ├── .env # Environment variables (ignored)
│ └── requirements.txt # Python dependencies
├── frontend/
│ ├── app/
│ │ ├── components/ # React components
│ │ │ ├── WeatherWidget.jsx
│ │ │ ├── NewsWidget.jsx
│ │ │ └── QuoteWidget.jsx
│ │ ├── page.js # Main dashboard page
│ │ └── globals.css # Global styles
│ ├── public/ # Static assets
│ ├── package.json # Node.js dependencies
│ └── .env.local # Frontend environment variables
├── render.yaml # Render deployment configuration
└── README.md # Project documentation

text

---

## 📦 Installation & Setup

### Prerequisites

- Python 3.10+
- Node.js 18+
- Redis (local or Upstash cloud)
- Git

### Backend Setup

1. **Clone the repository:**

```bash
git clone https://github.com/vinay-jawahrani/API-gateway.git
cd API-gateway/backend
Create and activate a virtual environment:

bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
Install dependencies:

bash
pip install -r requirements.txt
Create a .env file:

env
WEATHER_API_KEY=your_openweather_api_key
NEWS_API_KEY=your_newsapi_key
REDIS_URL=rediss://default:your_token@your_endpoint.upstash.io:6379
Run the backend server:

bash
uvicorn app.main:app --reload
Backend will be available at http://localhost:8000

Frontend Setup
Navigate to the frontend folder:

bash
cd ../frontend
Install dependencies:

bash
npm install
Create a .env.local file:

env
NEXT_PUBLIC_API_URL=http://localhost:8000
Run the frontend development server:

bash
npm run dev
Frontend will be available at http://localhost:3000

🧪 API Testing
Get Weather
bash
curl "http://localhost:8000/weather?city=London"
Get News
bash
curl "http://localhost:8000/news?limit=3"
Get Random Quote
bash
curl "http://localhost:8000/quotes"
Get Aggregated Dashboard
bash
curl "http://localhost:8000/dashboard"
Health Check
bash
curl "http://localhost:8000/health"
🐳 Docker Deployment (Optional)
Backend Dockerfile
dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
Build and Run
bash
docker build -t api-gateway-backend .
docker run -p 8000:8000 api-gateway-backend
🚀 Deployment
Backend (Render)
Push your code to GitHub.

On Render, click "New +" → "Web Service".

Connect your repository and set:

Root Directory: backend

Build Command: pip install -r requirements.txt

Start Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT

Add environment variables:

WEATHER_API_KEY

NEWS_API_KEY

REDIS_URL

Click "Create Web Service".

Frontend (Vercel)
Push your code to GitHub.

On Vercel, click "Add New" → "Project".

Import your repository and set:

Framework Preset: Next.js

Root Directory: frontend

Add environment variable:

NEXT_PUBLIC_API_URL: https://your-backend-url.onrender.com

Click "Deploy".

🔐 Environment Variables
Variable	Description	Required
WEATHER_API_KEY	OpenWeatherMap API key	❌ (optional)
NEWS_API_KEY	NewsAPI key	✅
REDIS_URL	Upstash Redis connection URL	❌ (fallback works)
NEXT_PUBLIC_API_URL	Backend URL for frontend	✅
🎯 Live Demo
Frontend: https://api-gateway-nine-theta.vercel.app

Backend API: https://api-gateway-masj.onrender.com

Swagger Docs: https://api-gateway-masj.onrender.com/docs

📄 License
MIT

👤 Author
Vinay Jawahrani

GitHub: @vinay-jawahrani

LinkedIn: linkedin.com/in/vinay-jawahrani

🌟 Show Your Support
If you found this project useful, give it a ⭐ on GitHub!

text

---

## ✅ How to Add This

1. Open `README.md` in your project root.
2. Replace everything with the above content.
3. Update the live URLs with your actual deployed URLs:
   - Frontend: `https://api-gateway-nine-theta.vercel.app`
   - Backend: `https://api-gateway-masj.onrender.com`
4. Save the file.
5. Push to GitHub:

```bash
git add README.md
git commit -m "Add complete README for API Gateway project"
git push
