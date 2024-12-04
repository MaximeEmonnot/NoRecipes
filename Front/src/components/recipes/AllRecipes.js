import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import "../../styles/AllRecipes.css";
import RecipeCard from './RecipeCard';
import axios from 'axios';

function RecipeList() {
  const { title } = useParams();
  const [recipes, setRecipes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchRecipes = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/databaseTest/recipes/by_category/${title}`);
        if (response.data && response.data.recettes) {
          let recipesData = response.data.recettes;
          if (!Array.isArray(recipesData)) {
            recipesData = [recipesData];
          }
          setRecipes(recipesData);
        } else {
          setError('Données non disponibles');
        }
        setLoading(false);
      } catch (err) {
        setError('Erreur lors de la récupération des recettes');
        setLoading(false);
      }
    };

    fetchRecipes();
  }, [title]);

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
              {recipes.length > 0 ? (
                recipes.map((recipe, index) => {
                  const imgSrc = recipe.images && recipe.images.length > 0
                    ? (recipe.images[0].startsWith('http') || recipe.images[0].startsWith('https') // Image externe
                      ? recipe.images[0] // On utilise directement l'url de l'image
                      : `http://localhost:8000/media/${recipe.images[0]}` // Si c'est une image locale, on utilise le chemin local
                    )
                    : 'default-image.jpg'; 
                  return (
                    <RecipeCard
                      key={index}
                      title={recipe.titre}
                      description={recipe.description}
                      imgSrc={imgSrc}
                      color="#FFFFFF"
                    />
                  );
                })
              ) : (
                <p>Aucune recette trouvée.</p>
              )}
            </section>
        </div>
    </div>
  );
}

export default RecipeList;
