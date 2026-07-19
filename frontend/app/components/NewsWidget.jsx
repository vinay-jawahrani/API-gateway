'use client';

import { useState, useEffect } from 'react';
import axios from 'axios';

export default function NewsWidget() {
    const [news, setNews] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const fetchNews = async () => {
        setLoading(true);
        setError(null);
        try {
            const response = await axios.get(
                `${process.env.NEXT_PUBLIC_API_URL}/weather?city=${city}`);
            setNews(response.data);
        } catch (err) {
            setError('Failed to fetch news');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchNews();
    }, []);

    if (loading) return <div className="widget loading">Loading news...</div>;
    if (error) return <div className="widget error">{error}</div>;

    return (
        <div className="widget news-widget">
            <h2>📰 Top News</h2>
            <button onClick={fetchNews} className="refresh-btn">Refresh</button>
            {news && news.data && news.data.articles && (
                <ul>
                    {news.data.articles.map((article, index) => (
                        <li key={index}>
                            <a href={article.url} target="_blank" rel="noopener noreferrer">
                                <strong>{article.title}</strong>
                            </a>
                            <p>{article.source}</p>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
}