import React, { useState } from 'react';
import '../styles/AdvancedSearch.css';
import { useNavigate } from 'react-router-dom';

const AdvancedSearch = ({ onSearch }) => {
    const [filters, setFilters] = useState({
        titre: '',
        ingredients: '',
        cuisineType: '',
        origin: '',
        dishType: '',
        rating: ''
    });

    const navigate = useNavigate();

    // Gestion des champs du formulaire
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFilters({
            ...filters,
            [name]: value,
        });
    };


    const handleSubmit = (e) => {
        e.preventDefault();
      
        if(filters.ingredients.length != 0)
            filters.ingredients = filters.ingredients.replace(" ", "")

        // Construction de la recherche via les filtres
        let search = "";
        if(filters.titre || filters.ingredients || filters.cuisineType || filters.origin || filters.dishType || filters.rating)
        {
            const params = new URLSearchParams();

            if(filters.titre)       params.append("titre", filters.titre);
            if(filters.ingredients) params.append("ingredients", filters.ingredients);
            if(filters.cuisineType) params.append("cuisine", filters.cuisineType);
            if(filters.origin)      params.append("origine", filters.origin);
            if(filters.dishType)    params.append("plat", filters.dishType);
            if(filters.rating)      params.append("note", filters.rating);

            search = params.toString();
        }

        navigate({
            pathname: "/AdvancedSearchRecipeList",
            search: search
        })
        
        if (onSearch) {
            onSearch(filters); 
        }
    };

    return (
        <div className="advanced-search">
            <h2>Recherche avancée</h2>
            <form onSubmit={handleSubmit}>
                {/* Par nom */}
                <div className="form-group">
                    <label>Par nom :</label>
                    <input 
                        type="text"
                        name="titre"
                        placeholder="Ex: Salade"
                        value={filters.titre}
                        onChange={handleChange}
                    />
                </div>

                {/* Par ingrédients */}
                <div className="form-group">
                    <label>Par ingrédients :</label>
                    <input
                        type="text"
                        name="ingredients"
                        placeholder="Ex: chocolat, fraise"
                        value={filters.ingredients}
                        onChange={handleChange}
                    />
                </div>

                {/* Par type de cuisine */}
                <div className="form-group">
                    <label>Par type de cuisine :</label>
                    <select name="cuisineType" value={filters.cuisineType} onChange={handleChange}>
                        <option value="">-- Sélectionner --</option>
                        <option value="française">Française</option>
                        <option value="italienne">Italienne</option>
                        <option value="asiatique">Asiatique</option>
                        <option value="orientale">Orientale</option>
                        <option value="américaine">Américaine</option>
                    </select>
                </div>

                {/* Par origine */}
                <div className="form-group">
                    <label>Par origine :</label>
                    <input
                        type="text"
                        name="origin"
                        placeholder="Ex: Italie, Japon"
                        value={filters.origin}
                        onChange={handleChange}
                    />
                </div>

                {/* Par type de plat */}
                <div className="form-group">
                    <label>Par type de plat :</label>
                    <select name="dishType" value={filters.dishType} onChange={handleChange}>
                        <option value="">-- Sélectionner --</option>
                        <option value="entrée">Entrée</option>
                        <option value="plat principal">Plat principal</option>
                        <option value="dessert">Dessert</option>
                        <option value="petit déjeuner">Viennoiserie</option>
                    </select>
                </div>

                {/* Par note */}
                <div className="form-group">
                    <label>Par note :</label>
                    <input
                        type="number"
                        name="rating"
                        placeholder="Note minimum (ex: 4)"
                        value={filters.rating}
                        onChange={handleChange}
                        min="1"
                        max="5"
                        step="0.1"
                    />
                </div> 

                <button type="submit" className="search-button">Rechercher</button>
            </form>
        </div>
    );
};

export default AdvancedSearch;