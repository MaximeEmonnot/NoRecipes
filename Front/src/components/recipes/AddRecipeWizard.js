import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const AddRecipeWizard = () => {
    const [currentStep, setCurrentStep] = useState(1); 
    const [recipe, setRecipe] = useState(null); 
    const navigate = useNavigate();

    // Fonction pour passer à l'étape suivante
    const handleNextStep = () => {
        setCurrentStep((prev) => prev + 1);
    };

    // Fonction pour retourner à l'accueil après la fin
    const handleFinish = () => {
        navigate("/");
    };

    // Gestion des différentes étapes
    return (
        <div className="add-recipe-wizard">
            {currentStep === 1 && <AddRecipe onRecipeCreated={setRecipe} onNext={handleNextStep} />}
            {currentStep === 2 && <SelectCategory recipe={recipe} onNext={handleNextStep} />}
            {currentStep === 3 && <AddIngredient recipe={recipe} onNext={handleNextStep} />}
            {currentStep === 4 && <AddUtensil recipe={recipe} onFinish={handleFinish} />}
        </div>
    );
};

export default AddRecipeWizard;
