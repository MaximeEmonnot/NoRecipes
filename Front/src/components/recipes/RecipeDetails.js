import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import '../../styles/RecipeDetails.css';

const RecipeDetails = () => {
    const { title } = useParams();
    const [recipe, setRecipe] = useState(null);
    const [ingredients, setIngredients] = useState([]);
    const [categorie, setCategory] = useState([]);
    const [utensils, setUtensils] = useState([]);
    const [comments, setComments] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchRecipeData = async () => {
            try {
                // Récupérer la recette
                const recipeResponse = await axios.get(`http://localhost:8000/databaseTest/recipes/${title}`);
                setRecipe(recipeResponse.data.recipe);

                // Récupérer la catégorie
                try {
                    const categorieReponse = await axios.get(`http://localhost:8000/databaseTest/categories/by_recipe/${title}`);
                    setCategory(categorieReponse.data.categorie.titre || "Non spécifiée");
                } catch (error) {
                    console.warn("Aucune catégorie trouvée pour cette recette.");
                }

                // Récupérer les ingrédients
                const ingredientsResponse = await axios.get(`http://localhost:8000/databaseTest/recipes/ingredients/${title}`);
                setIngredients(ingredientsResponse.data.ingredients);

                // Récupérer les ustensiles
                const utensilsResponse = await axios.get(`http://localhost:8000/databaseTest/recipes/utensils/${title}`);
                setUtensils(utensilsResponse.data.ustensiles);

                // Récupérer les commentaires
                const commentsResponse = await axios.get(`http://localhost:8000/databaseTest/comments/all/${title}`);
                setComments(commentsResponse.data.commentaires);

                setLoading(false);
            } catch (err) {
                setError("Erreur lors du chargement des données.");
                setLoading(false);
            }
        };

        fetchRecipeData();
    }, [title]);

    if (loading) {
        return <div>Chargement...</div>;
    }

    if (error) {
        return <div>{error}</div>;
    }

    return (
        <div className="recipe-details">
            {recipe && (
                <>
                    {/* Carrousel */}
                    <div className="image-container">
                        {recipe.images.length > 1 ? (
                            <div className="carousel">
                                {recipe.images.map((image, index) => (
                                    <div key={index} className="carousel-item">
                                        <img
                                            src={`http://localhost:8000/media/${image}`}
                                            alt={`Image ${index + 1} de ${recipe.titre}`}
                                        />
                                    </div>
                                ))}
                            </div>
                        ) : (
                            <div className="single-image">
                                <img
                                    src={`http://localhost:8000/media/${recipe.images[0]}`}
                                    alt={`Image de ${recipe.titre}`}
                                />
                            </div>
                        )}
                    </div>

                    {/* Détails de la recette */}
                    <div className="recipe-info">
                        <h1>{recipe.titre}</h1>               
                        <p><strong>Catégorie :</strong> {categorie}</p>
                        <p><strong>Origine :</strong> {recipe.origine}</p>
                        <p><strong>Description :</strong> {recipe.description}</p>
                        <p><strong>Note :</strong> {recipe.note}/5</p>
                        <p><strong>Temps de préparation :</strong> {recipe.temps_preparation} minutes</p>
                        <p><strong>Temps de cuisson :</strong> {recipe.temps_cuisson} minutes</p>
                        <p><strong>Temps de repos :</strong> {recipe.temps_repos} minutes</p>
                    </div>

                    {/* Liste des ingrédients */}
                    <div className="ingredients-section">
                        <h2>Ingrédients</h2>
                        <div className="ingredients-list">
                            {ingredients.map((ingredient, index) => (
                                <div key={index} className="ingredient-card">
                                    <p>{ingredient.quantite} {ingredient.type_unite} {ingredient.ingredient}</p>
                                </div>
                            ))}
                        </div>
                    </div>

                    {/* Liste des ustensiles */}
                    <div className="utensils-section">
                        <h2>Ustensiles</h2>
                        <div className="utensils-list">
                            {utensils.map((utensil, index) => (
                                <div key={index} className="utensil-card">
                                    <p>{utensil.nombre} x {utensil.utensil}</p>
                                </div>
                            ))}
                        </div>
                    </div>

                    {/* Liste des commentaires */}
                    <div className="comments-section">
                        <h2>Commentaires</h2>
                        {comments.length > 0 ? (
                            comments.map((comment, index) => (
                                <div key={index} className="comment-card">
                                    <p><strong>Note :</strong> {comment.note}/5</p>
                                    <p>{comment.texte}</p>
                                    {comment.images.length > 0 && (
                                        <img src={comment.images[0]} alt="Commentaire associé" />
                                    )}
                                </div>
                            ))
                        ) : (
                            <p>Aucun commentaire pour cette recette.</p>
                        )}
                    </div>
                </>
            )}
        </div>
    );
};

export default RecipeDetails;