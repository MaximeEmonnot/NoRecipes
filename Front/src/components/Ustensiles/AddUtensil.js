import React, { useState } from "react";
import "../../styles/AddUtensil.css"
import axios from 'axios';
import { useNavigate } from 'react-router-dom';


const AddUtensil = () => {
    const [formData, setFormData] = useState({
        titre: "",
        prix: "",
        description: "",
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
        formPayload.append("prix", formData.prix);
        formPayload.append("description", formData.description);

        for (let i = 0; i < formData.images.length; i++) {
            formPayload.append('images', formData.images[i]);
        }

        try {
            setIsLoading(true);
      
            // Envoi de la requête avec Axios
            const response = await axios.post(
              'http://localhost:8000/databaseTest/add_utensil',
              formPayload,
              {
                headers: {
                  'Content-Type': 'multipart/form-data', 
                },
              }
            );
      
            if (response.status === 200) {
                alert('Ustensile ajouté avec succès');
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
        <div className="add-utensil-container">
            <form className="add-utensil-form" onSubmit={handleSubmit}>
                <h2>Ajouter un Ustensile</h2>
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
                    <label htmlFor="origine">Prix</label>
                    <input
                        type="number"
                        id="prix"
                        name="prix"
                        step="0.01" 
                        value={formData.prix}
                        onChange={handleChange}
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

export default AddUtensil;