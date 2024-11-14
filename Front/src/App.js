import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import HomePage from './pages/HomePage';
import FormPage from './pages/FormPage'; 
import Footer from './components/Footer'
import './App.css'; 

const App = () => {
    return (
        <Router>
            <Navbar />
            <Routes>
                <Route path="/" element={<HomePage />} /> 
                <Route path="/form" element={<FormPage />} />
            </Routes>
            <Footer />
        </Router>
    );
};

export default App;
