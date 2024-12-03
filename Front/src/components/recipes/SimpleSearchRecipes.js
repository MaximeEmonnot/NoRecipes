import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import "../../styles/AllRecipes.css";
import RecipeCard from './RecipeCard';
import axios from 'axios';

function SimpleSearchRecipeList()
{
    const { search } = useParams();
    const [recipes, setRecipes] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchRecipes = async () => {
          try {
            const response = await axios.get(`http://localhost:8000/databaseTest/simple_recipe_search/${search}`);
            if (response.data && response.data.recipes) {
              let recipesData = response.data.recipes;
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
    }, [search]);
  
    if (loading) {
      return <div>Chargement des recettes...</div>;
    }
  
    if (error) {
      return <div>{error}</div>;
    }
  
    return (
      <div className='simple-search-recipes-container'>
        <h2>Liste des Recettes</h2>
        <div className="recipe-list">
              <section className="recipe-cards">
                {recipes.length > 0 ? (
                  recipes.map((recipe, index) => {
                    const imgSrc = recipe.images && recipe.images.length < 0 ? `http://localhost:8000/media/${recipe.images[0]}` : 'default-image.jpg';
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

export default SimpleSearchRecipeList;