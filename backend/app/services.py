import httpx
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Weather Service
async def get_weather(city: str = "London"):
    """Fetch weather data from OpenWeatherMap API"""
    if not WEATHER_API_KEY:
        return {"error": "Weather API key not configured"}
    
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params, timeout=10.0)
            if response.status_code == 200:
                data = response.json()
                return {
                    "city": data.get("name"),
                    "temperature": data.get("main", {}).get("temp"),
                    "condition": data.get("weather", [{}])[0].get("description"),
                    "humidity": data.get("main", {}).get("humidity"),
                    "wind_speed": data.get("wind", {}).get("speed")
                }
            else:
                return {"error": f"Weather API error: {response.status_code}"}
    except Exception as e:
        return {"error": f"Weather service unavailable: {str(e)}"}

# News Service
async def get_news(limit: int = 3):
    """Fetch news headlines from NewsAPI"""
    if not NEWS_API_KEY:
        return {"error": "News API key not configured"}
    
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",
        "apiKey": NEWS_API_KEY,
        "pageSize": limit
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params, timeout=10.0)
            if response.status_code == 200:
                data = response.json()
                articles = data.get("articles", [])
                return {
                    "total_results": data.get("totalResults", 0),
                    "articles": [
                        {
                            "title": article.get("title"),
                            "source": article.get("source", {}).get("name"),
                            "url": article.get("url"),
                            "published_at": article.get("publishedAt")
                        }
                        for article in articles
                    ]
                }
            else:
                return {"error": f"News API error: {response.status_code}"}
    except Exception as e:
        return {"error": f"News service unavailable: {str(e)}"}

# Quotes Service
async def get_quote():
    """Fetch a random quote from ZenQuotes API"""
    url = "https://zenquotes.io/api/random"
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=10.0)
            if response.status_code == 200:
                data = response.json()
                if data and len(data) > 0:
                    return {
                        "quote": data[0].get("q"),
                        "author": data[0].get("a")
                    }
                return {"error": "No quote available"}
            else:
                return {
                    "quote": "Success is not final, failure is not fatal: it is the courage to continue that counts.",
                    "author": "Winston Churchill"
                }
    except Exception as e:
        return {
            "quote": "The only way to do great work is to love what you do.",
            "author": "Steve Jobs"
        }