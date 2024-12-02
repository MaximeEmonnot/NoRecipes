import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import HomePage from './pages/HomePage';
import Footer from './components/Footer';
import './App.css'; 
import AddRecipe from './components/recipes/AddRecipe';
import AddIngredient from './components/Ingredients/AddIngredient';
import AddUtensil from './components/Ustensiles/AddUtensil';
import AddCategory from './components/Catégories/AddCategory';
import RecipeList from './components/recipes/AllRecipes';

const App = () => {
    return (
        <Router>
            <Navbar />
            <Routes>
                <Route path="/" element={<HomePage />} /> 
                <Route path='/AddRecipe' element={<AddRecipe />}/>
                <Route path='/AddIngredient' element={<AddIngredient />}/>
                <Route path='/AddUtensil' element={<AddUtensil />}/>
                <Route path='/AddCategory' element={<AddCategory />}/>
                <Route path='/AllRecipes' element={<RecipeList />}/>
            </Routes>
            <Footer />
        </Router>
    );
};

export default App;
