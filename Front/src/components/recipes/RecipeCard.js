import React from 'react';
import '../../styles/RecipeCard.css';

const RecipeCard = ({ title, description, imgSrc, color }) => {
    return (
       
        <div className="card" style={{ backgroundColor: color }}>
             {/*Composant pour afficher les fiches de recttes sur la page d'accueil*/}
            <img src={imgSrc} alt={title} />
            <h2>{title}</h2>
            <p>{description}</p>
            <button className="card-button">Voir la recette</button>
        </div>
    );
};

export default RecipeCard;
