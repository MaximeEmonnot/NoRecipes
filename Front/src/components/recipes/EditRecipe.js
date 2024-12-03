import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate, useParams } from "react-router-dom";

const EditRecipe = () => {
    const { title } = useParams(); // Récupère le titre de la recette depuis l'URL
    const navigate = useNavigate();

    const [recipeData, setRecipeData] = useState({
        origine: "",
        description: "",
        nombrePersonnes: 1,
        tempsPreparation: 0,
        tempsCuisson: 0,
    });

    const [images, setImages] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [isLoading, setIsLoading] = useState(false); 

    // Charger les données de la recette existante
    useEffect(() => {
        const fetchRecipe = async () => {
            try {
                const response = await axios.get(`http://localhost:8000/databaseTest/recipes/${title}`);
                const recipe = response.data.recipe;
                setRecipeData({
                    origine: recipe.origine,
                    description: recipe.description,
                    nombrePersonnes: recipe.nombre_personnes,
                    tempsPreparation: recipe.temps_preparation,
                    tempsCuisson: recipe.temps_cuisson,
                });
                setLoading(false);
            } catch (err) {
                console.error("Erreur lors du chargement de la recette :", err);
                setLoading(false);
            }
        };

        fetchRecipe();
    }, [title]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setRecipeData((prevData) => ({
            ...prevData,
            [name]: value,
        }));
    };

    const handleFileChange = (e) => {
        setImages(e.target.files);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();

        for (let key in recipeData) {
            formData.append(key, recipeData[key]);
        }

        Array.from(images).forEach((file) => {
            formData.append("images", file);
        });

        try {
            await axios.put(`http://localhost:8000/databaseTest/recipes/update/${title}`, formData, {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            });

            alert("Recette mise à jour avec succès !");

            navigate(`/RecipeDetails/${title}`); 
        } catch (err) {
            console.error("Erreur lors de la mise à jour de la recette :", err);

            alert("Erreur lors de la mise à jour de la recette.");
        }
    };

    if (loading) return <div>Chargement...</div>;

    return (
        <div className="add-recipe-container">
            <form className="add-recipe-form" onSubmit={handleSubmit}>
                <h2>Modifier la recette</h2>
                {error && <div className="error-message">{error}</div>}
                {isLoading && <div className="loading-message">Envoi en cours...</div>} 

                <div className="form-group">
                    <label htmlFor="origine">Origine</label>
                    <input
                        type="text"
                        id="origine"
                        name="origine"
                        value={recipeData.origine}
                        onChange={handleChange}
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="tempsPreparation">Temps de Préparation (min)</label>
                    <input
                        type="number"
                        id="tempsPreparation"
                        name="tempsPreparation"
                        value={recipeData.tempsPreparation}
                        onChange={handleChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="tempsCuisson">Temps de Cuisson (min)</label>
                    <input
                        type="number"
                        id="tempsCuisson"
                        name="tempsCuisson"
                        value={recipeData.tempsCuisson}
                        onChange={handleChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="nombrePersonnes">Nombre de Personnes</label>
                    <input
                        type="number"
                        id="nombrePersonnes"
                        name="nombrePersonnes"
                        value={recipeData.nombrePersonnes}
                        onChange={handleChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="description">Description</label>
                    <textarea
                        id="description"
                        name="description"
                        value={recipeData.description}
                        onChange={handleChange}
                        required
                    ></textarea>
                </div>

                <div className="form-group">
                    <label htmlFor="images">Images</label>
                    <input
                        type="file"
                        id="images"
                        name="images"
                        multiple
                        onChange={handleFileChange}
                    />
                </div>

                <button type="submit" className="submit-button" disabled={isLoading}>
                    {isLoading ? 'Modification en cours...' : 'Modifier'}
                </button>
            </form>
        </div>
    );
};

export default EditRecipe ;
