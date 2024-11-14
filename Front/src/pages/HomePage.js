import React from 'react';
import RecipeCard from '../components/RecipeCard';
import '../styles/HomePage.css';
import breakfastImage from '../images/breakfast.jpg';
import dessertImage from '../images/dessert.jpg';
import dinnerImage from '../images/dinner.jpg';
import banner from '../images/banner.jpg'

const HomePage = () => {
    return (
        <div className="home-page">
                <div className="hero-section">
                <img src={banner} alt="Bannière de recettes" className="banner-image" />
                </div>
            <section className="recipe-cards">
                <RecipeCard
                    title="Petit-déjeuner"
                    description="Découvrez nos recettes de petit-déjeuner."
                    imgSrc={breakfastImage}
                    color="#FFFFFF"
                />
                <RecipeCard
                    title="Desserts"
                    description="Découvrez nos recettes de desserts."
                    imgSrc={dessertImage}
                    color="#FFFFFF"
                />
                <RecipeCard
                    title="Plats"
                    description="Découvrez nos recettes de plats."
                    imgSrc={dinnerImage}
                    color="#FFFFFF"
                />
            </section>
        </div>
    );
};

export default HomePage;
