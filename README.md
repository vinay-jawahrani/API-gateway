# API Gateway with Service Aggregation

[![Live Demo](https://img.shields.io/badge/Live_Demo-View_API-blue)](https://api-gateway-ci1v.onrender.com/docs)
[![GitHub](https://img.shields.io/badge/GitHub-Repo-black)](https://github.com/vinay-jawahrani/api-gateway)

A FastAPI-based API Gateway that aggregates data from multiple external APIs (Weather, News, Quotes) into a single response with Redis caching.

## 🚀 Features

- **Service Aggregation** – Fetch weather, news, and quotes in one call (`/dashboard`)
- **Redis Caching** – Store API responses for 5 minutes to reduce external calls
- **Async Requests** – Parallel API calls for faster response times
- **Source Tracking** – Know whether data comes from cache or live API
- **Auto-generated Docs** – Swagger UI at `/docs`
- **Modular Design** – Separate services for each API

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **HTTP Client**: httpx (async)
- **Caching**: Redis (Upstash)
- **Environment**: python-dotenv
- **Deployment**: Render

## 📌 API Endpoints

| Method | Endpoint | Description | Cached |
|--------|----------|-------------|--------|
| GET | `/` | Welcome message | ❌ |
| GET | `/health` | Health check + Redis status | ❌ |
| GET | `/weather?city=London` | Get weather data | ✅ (5 min) |
| GET | `/news?limit=3` | Get top news headlines | ✅ (5 min) |
| GET | `/quotes` | Get random quote | ✅ (5 min) |
| GET | `/dashboard` | Aggregate all services | ❌ |

## 📦 Installation & Setup

### Prerequisites
- Python 3.10+
- Git
- Redis (local or cloud)

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/api-gateway.git
   cd api-gateway

   Create and activate virtual environment:

bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
Install dependencies:

bash
pip install -r requirements.txt
Create .env file:

text
WEATHER_API_KEY=your_openweather_key
NEWS_API_KEY=your_newsapi_key
REDIS_URL=rediss://default:your_token@your_endpoint.upstash.io:6379
Run the server:

bash
uvicorn app.main:app --reload
Access the API:

API: http://127.0.0.1:8000

Swagger Docs: http://127.0.0.1:8000/docs

🧪 API Testing
Get Weather
bash
curl "http://127.0.0.1:8000/weather?city=London"
Get News
bash
curl "http://127.0.0.1:8000/news?limit=3"
Get Random Quote
bash
curl "http://127.0.0.1:8000/quotes"
Get Aggregated Dashboard
bash
curl "http://127.0.0.1:8000/dashboard"
Health Check
bash
curl "http://127.0.0.1:8000/health"
📁 Project Structure
text
api-gateway/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   ├── services.py      # External API calls
│   └── cache.py         # Redis caching logic
├── venv/                # Virtual environment (ignored)
├── .env                 # Environment variables (ignored)
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
🔐 Environment Variables
Variable	Description	Required
WEATHER_API_KEY	OpenWeatherMap API key	❌ (optional)
NEWS_API_KEY	NewsAPI key	✅
REDIS_URL	Upstash Redis connection URL	❌ (fallback works)
🐳 Deployment
This project is deployed on Render:

Connect your GitHub repository

Set Build Command: pip install -r requirements.txt

Set Start Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT

Add environment variables in Render dashboard

Deploy and get a live URL

🎯 Live Demo
API URL: https://api-gateway-ci1v.onrender.com

Swagger Docs: https://api-gateway-ci1v.onrender.com/docs

📄 License
MIT

👤 Author
Vinay Jawahrani

GitHub: @vinay-jawahrani

🌟 Show Your Support
If you found this project useful, give it a ⭐ on GitHub!

