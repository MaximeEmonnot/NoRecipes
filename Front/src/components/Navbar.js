import React from 'react';
import '../styles/Navbar.css';
import logo from '../images/LogoSite.png'; 
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBars, faSearch, faUser } from '@fortawesome/free-solid-svg-icons';
import { Link } from 'react-router-dom'; 

const Navbar = () => {
    return (
        <nav className="navbar">
            <div className="navbar-left">
                {/* Icône de menu */}
                <button className="menu-icon">
                    <FontAwesomeIcon icon={faBars} />
                </button>
                
                {/* Logo redirection vers la page d'accueil */}
                <Link to="/" className="navbar-logo-link">
                    <img src={logo} alt="Logo" className="navbar-logo" />
                </Link>
            </div>
            
            {/* Barre de recherche */}
            <div className="search-container">
                <input type="text" className="search-input" placeholder="Rechercher une recette..." />
                {/* Icône de recherche */}
                <span className="search-icon">
                    <FontAwesomeIcon icon={faSearch} />
                </span>
            </div>
            
            <Link to="/form" className="connexion-button">
                <span className="user-icon">
                    <FontAwesomeIcon icon={faUser} />
                </span> Connexion
            </Link>
        </nav>
    );
};

export default Navbar;
