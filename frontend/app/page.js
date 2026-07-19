import WeatherWidget from './components/WeatherWidget';
import NewsWidget from './components/NewsWidget';
import QuoteWidget from './components/QuoteWidget';

export default function Home() {
    return (
        <main className="dashboard">
            <h1>📊 Live Dashboard</h1>
            <div className="widget-grid">
                <WeatherWidget />
                <NewsWidget />
                <QuoteWidget />
            </div>
        </main>
    );
}