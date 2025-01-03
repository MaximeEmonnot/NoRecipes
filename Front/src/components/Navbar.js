import React, { useState } from 'react';
import '../styles/Navbar.css';
import logo from '../images/LogoSite.png';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBars, faSearch, faFilter } from '@fortawesome/free-solid-svg-icons';
import { Link } from 'react-router-dom';
import AdvancedSearch from './AdvancedSearch'; 
import { useNavigate } from 'react-router-dom';

const Navbar = () => {
    const [menuOpen, setMenuOpen] = useState(false); 
    const [searchOpen, setSearchOpen] = useState(false); 
    const [searchQuery, setSearchQuery] = useState(''); 

    const navigate = useNavigate();
  
    const toggleMenu = () => {
        setMenuOpen(!menuOpen);
    };

    const toggleSearch = () => {
        setSearchOpen(!searchOpen);
    };

    // Fonction pour gérer la recherche
    const handleSearch = async () => {
        if(searchQuery.length != 0)
        {
            console.log('Recherche effectuée pour:', searchQuery);   
            navigate(`/SimpleSearchRecipeList/${searchQuery}`);
        }
    };

    return (
        <nav className="navbar">
            <div className="navbar-left">
                {/* Icône de menu burger */}
                <button className="menu-icon" onClick={toggleMenu}>
                    <FontAwesomeIcon icon={faBars} />
                </button>

                {/* Logo redirection vers la page d'accueil */}
                <Link to="/" className="navbar-logo-link">
                    <img src={logo} alt="Logo" className="navbar-logo" />
                </Link>
            </div>

            {/* Conteneur pour la recherche et le bouton Filtrer */}
            <div className="search-filter-container">
                {/* Barre de recherche */}
                <div className="search-container">
                    <input 
                        type="text" 
                        className="search-input" 
                        placeholder="Rechercher une recette..." 
                        value={searchQuery} 
                        onChange={(e) => setSearchQuery(e.target.value)} 
                    />
                    {/* Icône de recherche cliquable */}
                    <button className="search-icon" onClick={handleSearch}>
                        <FontAwesomeIcon icon={faSearch} />
                    </button>
                </div>

                {/* Icône de filtre */}
                <div className="advanced-search-container">
                    <button className="filter-icon" onClick={toggleSearch}>
                        <FontAwesomeIcon icon={faFilter} />
                        Filtrer
                    </button>
                </div>
            </div>

            {/* Affiche le composant de recherche avancée*/}
            {searchOpen && <AdvancedSearch />}

            {/* Menu déroulant */}
            {menuOpen && (
                <div className="dropdown-menu">
                    <ul>
                        <li><Link to="#">Recettes populaires</Link></li>
                        <li><Link to="#">Recettes les mieux notées</Link></li>
                        <li>Recettes par catégories
                            <ul>
                                <li><Link to="#">Apéritifs</Link></li>
                                <li><Link to="#">Entrées</Link></li>
                                <li><Link to="#">Plats</Link></li>
                                <li><Link to="#">Desserts</Link></li>
                                <li><Link to="#">Boissons</Link></li>
                                <li><Link to="#">Petit déjeuner</Link></li>
                            </ul>
                        </li>
                    </ul>
                </div>
            )}
        </nav>
    );
};

export default Navbar;
