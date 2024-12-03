import React, { useState, useEffect } from 'react';
import { useLocation, useParams } from 'react-router-dom';
import "../../styles/AllRecipes.css";
import RecipeCard from './RecipeCard';
import axios from 'axios';

function AdvancedSearchRecipeList()
{
    const params      = new URLSearchParams(useLocation().search);
    const titre       = params.get("titre");
    const ingredients = params.get("ingredients");
    const cuisine     = params.get("cuisine");
    const origine     = params.get("origine");
    const plat        = params.get("plat");
    const note        = params.get("note");

    const [recipes, setRecipes] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchRecipes = async () => {
          try {

            const params = {
              search: titre,
              ingredient_list: ingredients,
              cuisine_type: cuisine,
              origin: origine,
              min_rate: note
            }

            const response = await axios.get('http://localhost:8000/databaseTest/advanced_recipe_search/', {params: params});
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
    }, [titre, ingredients, cuisine, origine, plat, note]);
  
    if (loading) {
      return <div>Chargement des recettes...</div>;
    }
  
    if (error) {
      return <div>{error}</div>;
    }
  
    return (
      <div className='advanced-search-recipes-container'>
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

export default AdvancedSearchRecipeList;