import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import CategoryCard from '../components/Catégories/CategoryCard';
import '../styles/HomePage.css';
import breakfastImage from '../images/breakfast.jpg';
import dessertImage from '../images/dessert.jpg';
import dinnerImage from '../images/dinner.jpg';
import banner from '../images/banner.jpg'
import aperitifImage from '../images/aperitifs.jpg'
import boissonsImage from '../images/boissons.jpg'
import entreeImage from '../images/entree.jpg'
import axios from 'axios';

const HomePage = () => {
    const { title } = useParams();
    const navigate = useNavigate();
    const [categories, setCategory] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
  
    useEffect(() => {
      const fetchRecipes = async () => {
        try {
          const response = await axios.get(`http://localhost:8000/databaseTest/categories/`);
          if (response.data && response.data.categories) {
            let categoriesData = response.data.categories;

            if (!Array.isArray(categoriesData)) {
                categoriesData = [categoriesData];
            }

            setCategory(categoriesData);

          } else {
            setError('Données non disponibles');
          }

          setLoading(false);
        } catch (err) {
          setError('Erreur lors de la récupération des catégories');
          setLoading(false);
        }
      };
  
      fetchRecipes();
    }, [title]);

    const handleAddRecipe = () => {
        navigate(`/AddRecipe`); 
    };
  
    if (loading) {
      return <div>Chargement des catégories...</div>;
    }
  
    if (error) {
      return <div>{error}</div>;
    }
   
    return (
        <div className="home-page">
            <div className="hero-section">
                <img src={banner} alt="Bannière de recettes" className="banner-image" />
            </div>
            <div className="recipe-action-button">
                <button onClick={handleAddRecipe} className="edit-recipe-button">Ajouter la recette</button>
            </div>
            <section className="recipe-cards">
                {categories.length > 0 ? (
                    categories.map((category, index) => {
                        const imgSrc = category.images && category.images.length > 0
                        ? (category.images[0].startsWith('http') || category.images[0].startsWith('https') // Image externe
                        ? category.images[0] // On utilise directement l'url de l'image
                        : `http://localhost:8000/media/${category.images[0]}` // Si c'est une image locale, on utilise le chemin local
                        )
                        : 'default-image.jpg'; 
                    return (
                        <CategoryCard
                        key={index}
                        title={category.titre}
                        description="Découvrez les recettes"
                        imgSrc={imgSrc}
                        color="#FFFFFF"
                        />
                    );
                    })
                ) : (
                    <p>Aucune catégorie trouvée.</p>
                )}
            </section>
        </div>
    );
};

export default HomePage;
