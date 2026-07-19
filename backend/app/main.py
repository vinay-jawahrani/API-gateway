from fastapi import FastAPI
from app.services import get_weather, get_news, get_quote
from app.cache import cache

app = FastAPI(
    title="API Gateway",
    description="API Gateway with service aggregation and caching",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "API Gateway is running!"}

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "redis": "connected" if cache.is_connected() else "not available"
    }

@app.get("/weather")
async def weather(city: str = "London"):
    """Get weather data for a city (cached for 5 minutes)"""
    cache_key = f"weather:{city.lower()}"
    
    cached = await cache.get(cache_key)
    if cached:
        return {"source": "cache", "data": cached}
    
    data = await get_weather(city)
    if "error" not in data:
        await cache.set(cache_key, data, ttl=300)
    return {"source": "api", "data": data}

@app.get("/news")
async def news(limit: int = 3):
    """Get top news headlines (cached for 5 minutes)"""
    cache_key = f"news:{limit}"
    
    cached = await cache.get(cache_key)
    if cached:
        return {"source": "cache", "data": cached}
    
    data = await get_news(limit)
    if "error" not in data:
        await cache.set(cache_key, data, ttl=300)
    return {"source": "api", "data": data}

@app.get("/quotes")
async def quotes():
    """Get a random quote (cached for 5 minutes)"""
    cache_key = "quote:random"
    
    cached = await cache.get(cache_key)
    if cached:
        return {"source": "cache", "data": cached}
    
    data = await get_quote()
    if "error" not in data:
        await cache.set(cache_key, data, ttl=300)
    return {"source": "api", "data": data}

@app.get("/dashboard")
async def dashboard():
    """Get aggregated data from all services"""
    weather_data = await get_weather()
    news_data = await get_news()
    quote_data = await get_quote()
    
    return {
        "weather": weather_data,
        "news": news_data,
        "quote": quote_data
    }

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://api-gateway-frontend.vercel.app",   # Your Vercel URL
        "https://api-gateway-frontend-git-main.vercel.app",  # Preview URL (optional)
        "https://api-gateway-frontend.vercel.app"    # Add with and without trailing slash
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)