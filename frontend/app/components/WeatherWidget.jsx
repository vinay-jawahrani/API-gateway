'use client';

import { useState, useEffect } from 'react';
import axios from 'axios';

export default function WeatherWidget() {
    const [weather, setWeather] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [city, setCity] = useState('London');

    const fetchWeather = async () => {
        setLoading(true);
        setError(null);
        try {
            const response = await axios.get(`http://localhost:8000/weather?city=${city}`);
            setWeather(response.data);
        } catch (err) {
            setError('Failed to fetch weather data');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchWeather();
    }, []);  // Runs only once on mount

    return (
        <div className="widget weather-widget">
            <h2>🌤️ Weather</h2>
            <div>
                <input 
                    type="text" 
                    value={city} 
                    onChange={(e) => setCity(e.target.value)}
                    placeholder="Enter city"
                    className="city-input"
                />
                <button onClick={fetchWeather} className="refresh-btn">Refresh</button>
            </div>
            {loading && <div>Loading weather...</div>}
            {error && <div className="error">{error}</div>}
            {weather && weather.data && (
                <div className="weather-data">
                    <p><strong>{weather.data.city}</strong></p>
                    <p>🌡️ {weather.data.temperature}°C</p>
                    <p>☁️ {weather.data.condition}</p>
                    <p>💨 {weather.data.wind_speed} km/h</p>
                </div>
            )}
        </div>
    );
}