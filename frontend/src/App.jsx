import React from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import HomePage from './pages/HomePage';
import './App.css';

function App() {
  return (
    <div className="app-shell">
      <Header />
      <main className="app-main">
        <HomePage />
      </main>
      <Footer />
    </div>
  );
}

export default App;
