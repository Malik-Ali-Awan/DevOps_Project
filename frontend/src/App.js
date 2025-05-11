import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [quotes, setQuotes] = useState([]);
  const [newQuote, setNewQuote] = useState('');
  const [error, setError] = useState('');

  const API_URL = process.env.REACT_APP_API_URL || 'http://quote-api';

  //const API_URL = process.env.REACT_APP_API_URL || '/api';


  useEffect(() => {
    fetchQuotes();
  }, []);

  const fetchQuotes = async () => {
    try {
      const response = await axios.get(`${API_URL}/api/quotes`);
      setQuotes(response.data);
    } catch (err) {
      setError('Failed to fetch quotes');
      console.error('Error fetching quotes:', err);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!newQuote.trim()) return;

    try {
      await axios.post(`${API_URL}/api/quotes`, { text: newQuote });
      setNewQuote('');
      fetchQuotes();
    } catch (err) {
      setError('Failed to submit quote');
      console.error('Error submitting quote:', err);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Quote Saver</h1>
      </header>
      <main>
        <section className="quote-form">
          <h2>Submit a New Quote</h2>
          <form onSubmit={handleSubmit}>
            <input
              type="text"
              value={newQuote}
              onChange={(e) => setNewQuote(e.target.value)}
              placeholder="Enter your quote here..."
              required
            />
            <button type="submit">Save Quote</button>
          </form>
        </section>

        <section className="quotes-list">
          <h2>Saved Quotes</h2>
          {error && <p className="error">{error}</p>}
          <ul>
            {quotes.map((quote) => (
              <li key={quote.id}>{quote.text}</li>
            ))}
          </ul>
        </section>
      </main>
    </div>
  );
}

export default App; 