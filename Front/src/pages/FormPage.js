import React, { useState } from 'react';
import '../styles/FormPage.css'; 

const FormPage = () => {
    const [isLogin, setIsLogin] = useState(true); 

    return (
        <div className="container">
            {isLogin ? (
                <div className="connect">
                    <div className="left">
                        <h1>Bonjour !</h1>
                        <p>Si vous n'avez pas de compte <br /> Inscrivez-vous !</p>
                        <button onClick={() => setIsLogin(false)}>S'inscrire</button>
                    </div>
                    <div className="right">
                        <h1>Connexion</h1>
                        <form className="form">
                            <input type="email" placeholder="Email" required />
                            <input type="password" placeholder="Mot de passe" required />
                        </form>
                        <button>Se connecter</button>
                    </div>
                </div>
            ) : (
                <div className="inscription">
                    <div className="left">
                        <h1>Bon retour !</h1>
                        <p>Connectez-vous avec votre compte <br /> pour nous rejoindre !</p>
                        <button onClick={() => setIsLogin(true)}>Se connecter</button>
                    </div>
                    <div className="right">
                        <h1>Créer un compte</h1>
                        <form className="form">
                            <input type="text" placeholder="Pseudo" required />
                            <input type="email" placeholder="Email" required />
                            <input type="text" placeholder="Nom" />
                            <input type="text" placeholder="Prenom" />
                            <input type="password" placeholder="Mot de passe" required />
                            <input type="password" placeholder="Confirmez mot de passe" required />
                        </form>
                        <button>S'inscrire</button>
                    </div>
                </div>
            )}
        </div>
    );
};

export default FormPage;
