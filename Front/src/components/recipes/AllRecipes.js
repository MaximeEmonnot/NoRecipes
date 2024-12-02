import React, { useState, useEffect } from 'react';
import "../../styles/AllRecipes.css";
import RecipeCard from './RecipeCard';
import axios from 'axios';

function RecipeList() {
  const [recipes, setRecipes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchRecipes = async () => {
      try {
        const response = await axios.get('http://localhost:8000/databaseTest/recipes/');
        setRecipes(response.data.recipes);
        setLoading(false);
      } catch (err) {
        setError('Erreur lors de la récupération des recettes');
        setLoading(false);
      }
    };

    fetchRecipes();
  }, []);

  if (loading) {
    return <div>Chargement des recettes...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <div className='all-recipes-container'>
      <h2>Liste des Recettes</h2>
      <div className="recipe-list">
            <section className="recipe-cards">
            {recipes.map((recipe, index) => {
                    const imgSrc = recipe.images && recipe.images.length > 0 ? `http://localhost:8000/media/${recipe.images[0]}` : 'default-image.jpg'; // Utilise une image par défaut si pas d'image
                    return (
                        <RecipeCard
                            key={index}
                            title={recipe.titre}  // Le titre de la recette
                            description={recipe.description}  // Description de la recette
                            imgSrc={imgSrc}  // L'URL de la première image ou une image par défaut
                            color="#FFFFFF"  // Choisir une couleur si nécessaire
                        />
                    );
                })}
            </section>
        </div>
    </div>
  );
}

export default RecipeList;
