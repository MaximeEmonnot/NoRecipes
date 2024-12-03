import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import '../../styles/RecipeDetails.css';

const RecipeDetails = () => {
    const { title } = useParams();
    const navigate = useNavigate();
    const [recipe, setRecipe] = useState(null);
    const [ingredients, setIngredients] = useState([]);
    const [categorie, setCategory] = useState([]);
    const [utensils, setUtensils] = useState([]);
    const [comments, setComments] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [showCommentForm, setShowCommentForm] = useState(false);
    const [commentText, setCommentText] = useState('');
    const [commentNote, setCommentNote] = useState(0);
    const [showConfirmDelete, setShowConfirmDelete] = useState(false);

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

    // Gérer l'ajout de commentaire
    const handleAddComment = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append("texte", commentText);
        formData.append("note", commentNote);
        try {
            await axios.post(`http://localhost:8000/databaseTest/comments/add/${title}/`, formData, {
                headers: {
                    "Content-Type": "multipart/form-data"
                }
            });
            // Recharger les commentaires
            const commentsResponse = await axios.get(`http://localhost:8000/databaseTest/comments/all/${title}`);
            setComments(commentsResponse.data.commentaires);
            setShowCommentForm(false);
            setCommentText('');
            setCommentNote(0);
        } catch (error) {
            console.error("Erreur lors de l'ajout du commentaire :", error);
            alert("Une erreur s'est produite lors d'ajout du commenetaire.");
        }
    };

    // Gérer la suppression de la recette
    const handleDeleteRecipe = async () => {
        try {
            await axios.delete(`http://localhost:8000/databaseTest/recipes/delete/${title}`);
            alert("Recette supprimée avec succès.");
            setShowConfirmDelete(false);
            navigate(-1); 
        } catch (error) {
            console.error("Erreur lors de la suppression de la recette :", error);
            alert("Une erreur s'est produite lors de la suppression.");
        }
    };

    // Gérer la redirection pour la modification
    const handleEditRecipe = () => {
        navigate(`/EditRecipe/${title}`); 
    };

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
                            {recipe.images.map((image, index) => {
                                // Vérification si l'image est locale ou externe
                                const imgSrc = image.startsWith('http') || image.startsWith('https')
                                ? image // URL externe
                                : `http://localhost:8000/media/${image}`; // Image locale

                                return (
                                <div key={index} className="carousel-item">
                                    <img
                                    src={imgSrc}
                                    alt={`Image ${index + 1} de ${recipe.titre}`}
                                    />
                                </div>
                                );
                            })}
                            </div>
                        ) : (
                            <div className="single-image">
                            {recipe.images.length > 0 && (
                                <img
                                src={
                                    recipe.images[0].startsWith('http') || recipe.images[0].startsWith('https')
                                    ? recipe.images[0] // URL externe
                                    : `http://localhost:8000/media/${recipe.images[0]}` // Image locale
                                }
                                alt={`Image de ${recipe.titre}`}
                                />
                            )}
                            </div>
                        )}
                    </div>

                    {/* Détails de la recette */}
                    <div className="recipe-info">
                        <h1>{recipe.titre}</h1>
                        <p><strong>Catégorie :</strong> {categorie}</p>
                        <p><strong>Origine :</strong> {recipe.origine}</p>
                        <p><strong>Description :</strong> {recipe.description}</p>
                        <p><strong>Nombre de personnes :</strong> {recipe.nombre_personnes}</p>
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

                        {/* Bouton pour ajouter un commentaire */}
                        <div className="actions">
                            <button onClick={() => setShowCommentForm(!showCommentForm)} className="add-comment-button">
                                Ajouter un commentaire
                            </button>
                            {showCommentForm && (
                                <form onSubmit={handleAddComment} className="comment-form">
                                    <textarea
                                        value={commentText}
                                        onChange={(e) => setCommentText(e.target.value)}
                                        placeholder="Votre commentaire"
                                        required
                                        className="comment-textarea"
                                    />
                                    <input
                                        type="number"
                                        value={commentNote}
                                        onChange={(e) => setCommentNote(e.target.value)}
                                        placeholder="Note sur 5"
                                        min="1"
                                        max="5"
                                        required
                                        className="comment-note"
                                    />
                                    <button type="submit" className="submit-comment-button">Valider</button>
                                </form>
                            )}
                        </div>
                    </div>

                    {/* Boutons pour modifier et supprimer */}
                    <div className="recipe-action-buttons">
                        <button onClick={handleEditRecipe} className="edit-recipe-button">Modifier la recette</button>
                        <button
                            onClick={() => setShowConfirmDelete(true)}
                            className="delete-recipe-button"
                        >
                            Supprimer la recette
                        </button>
                    </div>

                    {/* Boîte de confirmation pour suppression */}
                    {showConfirmDelete && (
                        <div className="confirm-delete-modal">
                            <div className="confirm-delete-content">
                                <p>Êtes-vous sûr de vouloir supprimer cette recette ?</p>
                                <div className="confirm-delete-buttons">
                                    <button
                                        onClick={handleDeleteRecipe}
                                        className="confirm-button"
                                    >
                                        Oui
                                    </button>
                                    <button
                                        onClick={() => setShowConfirmDelete(false)}
                                        className="cancel-button"
                                    >
                                        Non
                                    </button>
                                </div>
                            </div>
                        </div>
                    )}
                </>
            )}
        </div>
    );
};

export default RecipeDetails;
