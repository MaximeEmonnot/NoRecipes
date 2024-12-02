import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../../styles/CategoryCard.css';

const RecipeCard = ({ title, description, imgSrc, color }) => {
    const navigate = useNavigate(); 

    const handleViewRecipe = () => {
        navigate(`/AllRecipes/category/${title}`);
    };

    return (
       
        <div className="card" style={{ backgroundColor: color }}>
             {/*Composant pour afficher les fiches de recttes sur la page d'accueil*/}
            <img src={imgSrc} alt={title} />
            <h2>{title}</h2>
            <p>{description}</p>
            <button className="card-button" onClick={handleViewRecipe}>Voir les recettes</button>
        </div>
    );
};

export default RecipeCard;
