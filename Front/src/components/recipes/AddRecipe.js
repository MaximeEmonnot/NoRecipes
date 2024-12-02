import React, { useState } from "react";
import "../../styles/AddRecipe.css"
import axios from 'axios';
import { useNavigate } from 'react-router-dom';


const AddRecipe = () => {
    const [formData, setFormData] = useState({
        titre: "",
        origine: "",
        description: "",
        tempsPreparation: "",
        tempsCuisson: "",
        nombrePersonnes: "",
        images: [],
    });

    const [error, setError] = useState(null);
    const [isLoading, setIsLoading] = useState(false); 
    const navigate = useNavigate(); 

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    };

    const handleFileChange = (e) => {
        setFormData({ ...formData, images: e.target.files });
      };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const formPayload = new FormData();
        formPayload.append("titre", formData.titre);
        formPayload.append("origine", formData.origine);
        formPayload.append("description", formData.description);
        formPayload.append("tempsPreparation", formData.tempsPreparation);
        formPayload.append("tempsCuisson", formData.tempsCuisson);
        formPayload.append("nombrePersonnes", formData.nombrePersonnes);

        for (let i = 0; i < formData.images.length; i++) {
            formPayload.append('images', formData.images[i]);
        }

        try {
            setIsLoading(true); 
      
            // Envoi de la requête avec Axios
            const response = await axios.post(
              'http://localhost:8000/databaseTest/add_recipe',
              formPayload,
              {
                headers: {
                  'Content-Type': 'multipart/form-data', // Nécessaire pour envoyer des fichiers
                },
              }
            );
      
            if (response.status === 200) {
                alert('Recette ajoutée avec succès');
              navigate('/');
            } else {
              setError(response.data.error || 'Une erreur est survenue');
            }
        } catch (err) {
            setError(err.response?.data?.error || 'Erreur réseau ou serveur');
        } finally {
            setIsLoading(false); 
        }
    };

    return (
        <div className="add-recipe-container">
            <form className="add-recipe-form" onSubmit={handleSubmit}>
                <h2>Ajouter une Recette</h2>
                {error && <div className="error-message">{error}</div>}
                {isLoading && <div className="loading-message">Envoi en cours...</div>} 


                <div className="form-group">
                    <label htmlFor="titre">Titre</label>
                    <input
                        type="text"
                        id="titre"
                        name="titre"
                        value={formData.titre}
                        onChange={handleChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="origine">Origine</label>
                    <input
                        type="text"
                        id="origine"
                        name="origine"
                        value={formData.origine}
                        onChange={handleChange}
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="tempsPreparation">Temps de Préparation (min)</label>
                    <input
                        type="number"
                        id="tempsPreparation"
                        name="tempsPreparation"
                        value={formData.tempsPreparation}
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
                        value={formData.tempsCuisson}
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
                        value={formData.nombrePersonnes}
                        onChange={handleChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="description">Description</label>
                    <textarea
                        id="description"
                        name="description"
                        value={formData.description}
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
                    {isLoading ? 'Ajout en cours...' : 'Ajouter'}
                </button>
            </form>
        </div>
    );
};

export default AddRecipe;