import React from 'react';
import RecipeCard from '../components/RecipeCard';
import '../styles/HomePage.css';
import breakfastImage from '../images/breakfast.jpg';
import dessertImage from '../images/dessert.jpg';
import dinnerImage from '../images/dinner.jpg';
import banner from '../images/banner.jpg'
import aperitifImage from '../images/aperitifs.jpg'
import boissonsImage from '../images/boissons.jpg'
import entreeImage from '../images/entree.jpg'

const HomePage = () => {
    return (
        <div className="home-page">
                <div className="hero-section">
                <img src={banner} alt="Bannière de recettes" className="banner-image" />
                </div>
            <section className="recipe-cards">
            <RecipeCard
                    title="Apéritifs"
                    description="Découvrez nos recettes d'apéritifs."
                    imgSrc={aperitifImage}
                    color="#FFFFFF"
                />
                <RecipeCard
                    title="Entrées"
                    description="Découvrez nos recettes d'entrées."
                    imgSrc={entreeImage}
                    color="#FFFFFF"
                />
                <RecipeCard
                    title="Plats"
                    description="Découvrez nos recettes de plats."
                    imgSrc={dinnerImage}
                    color="#FFFFFF"
                />
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
                    title="Boissons"
                    description="Découvrez nos recettes de boissons."
                    imgSrc={boissonsImage}
                    color="#FFFFFF"
                />
                
            </section>
        </div>
    );
};

export default HomePage;