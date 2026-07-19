'use client';

import { useState, useEffect } from 'react';
import axios from 'axios';

export default function QuoteWidget() {
    const [quote, setQuote] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const fetchQuote = async () => {
        setLoading(true);
        setError(null);
        try {
            const response = await axios.get(
                `${process.env.NEXT_PUBLIC_API_URL}/weather?city=${city}`);
            setQuote(response.data);
        } catch (err) {
            setError('Failed to fetch quote');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchQuote();
    }, []);

    if (loading) return <div className="widget loading">Loading quote...</div>;
    if (error) return <div className="widget error">{error}</div>;

    return (
        <div className="widget quote-widget">
            <h2>💬 Quote</h2>
            <button onClick={fetchQuote} className="refresh-btn">New Quote</button>
            {quote && quote.data && (
                <div className="quote-content">
                    <p>"{quote.data.quote}"</p>
                    <p>— {quote.data.author}</p>
                </div>
            )}
        </div>
    );
}
export default function QuoteWidget() {
    console.log('🟢 QuoteWidget is rendering');  // Add this

    useEffect(() => {
        console.log('🟢 QuoteWidget useEffect fired');  // Add this
        fetchQuote();
    }, []);

    const fetchQuote = async () => {
        console.log('🟢 fetchQuote called');  // Add this
        // ... rest of the code
    };
}