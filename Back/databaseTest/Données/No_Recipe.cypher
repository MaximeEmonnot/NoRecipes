// Création des catégories
CREATE (cat1:Category {titre: 'Entrées', images: ['https://img.freepik.com/photos-gratuite/poulet-frit-aux-champignons-riz_140725-9648.jpg?t=st=1733177887~exp=1733181487~hmac=3b6c21ab205390dc9b4c96174706d6fff4cfee122010cfb03ab957e9e8549ee1&w=826']})
CREATE (cat2:Category {titre: 'Plats principaux', images: ['https://img.freepik.com/photos-gratuite/viande-sadj-legumes-verts-epices-vue-dessus_140725-9138.jpg?t=st=1733178005~exp=1733181605~hmac=4fddc9b19c45764043edad34abf9de33ebddda1c3bf9bc307c9a92e865fd9c84&w=996']})
CREATE (cat3:Category {titre: 'Desserts', images: ['https://img.freepik.com/photos-gratuite/angle-eleve-gateaux-plaque-macarons_23-2148489104.jpg?t=st=1733178037~exp=1733181637~hmac=95acc11b26359fc2cf2d88430a5c0519078208dcdcb5cd88134fbbac49373d61&w=360']})
CREATE (cat4:Category {titre: 'Végétarien', images: ['https://img.freepik.com/photos-gratuite/legumes-crus-noix-photographie-alimentaire-plat_53876-101574.jpg?t=st=1733178155~exp=1733181755~hmac=075fccb0c1b4484df82339e5407d479833aee635e4b56aa2af8a54e86d56f4c1&w=740']})
CREATE (cat5:Category {titre: 'Sans gluten', images: ['https://www.shutterstock.com/shutterstock/photos/1918282730/display_1500/stock-photo--gluten-free-sans-gluten-sign-handwritten-on-a-chalk-board-surrounded-by-ingrediients-close-up-1918282730.jpg']})
CREATE (cat6:Category {titre: 'Recettes rapides', images: ['https://img.freepik.com/photos-gratuite/vue-dessus-savoureuse-salade-poulet-aux-legumes_140725-85137.jpg?t=st=1733178246~exp=1733181846~hmac=09f1e77d9f51aa58553b6070679490d5823910becbf10193260c9a9819999fc1&w=1060']})
CREATE (cat7:Category {titre: 'Cuisine asiatique', images: ['https://img.freepik.com/photos-gratuite/gros-plan-delicieuse-cuisine-asiatique_23-2149091611.jpg?t=st=1733178287~exp=1733181887~hmac=24d4d6e947990823f22d03c6428057aee4b9d1f0f9ffed2b3e61431a34dbd1c9&w=360']})
CREATE (cat8:Category {titre: 'Cuisine méditerranéenne', images: ['https://img.freepik.com/photos-gratuite/fond-rustique-olives-du-fromage-tomates_23-2147612076.jpg?t=st=1733244575~exp=1733248175~hmac=c501a5edc66b4c4e35c3efe6679247d8cc29c055c974e0545f1867687d670614&w=1060']})
CREATE (cat9:Category {titre: 'Recettes de fête', images: ['https://img.freepik.com/photos-gratuite/vue-dessus-delicieux-gateaux-macarons-francais-fond-noir_140725-104585.jpg?t=st=1733178564~exp=1733182164~hmac=810c13bf253aba4b0e76a5e02c51b72ad39365ebda414bdf2f686f96a8f7125f&w=1060']})
CREATE (cat10:Category {titre: 'Soupes', images: ['https://img.freepik.com/photos-gratuite/soupe-aux-lentilles-servie-citron-legumes-verts_141793-781.jpg?t=st=1733178598~exp=1733182198~hmac=bcef320e8ca04ead7190d1a23587d8865723f1d1e2f39af95bf7e18ff646ab1a&w=360']})

// Création des recettes
CREATE (r1:Recipe {titre: 'Salade César', origine: 'Italie', note: 4.5, total_notes: 10, somme_notes: 45, description: 'Salade romaine avec poulet grillé et sauce César.', images: ['https://img.freepik.com/photos-gratuite/salade-saine-au-poulet-legumes_144627-14724.jpg?t=st=1733178638~exp=1733182238~hmac=5ea6ea5c2a3284ab8e03e0123a8fa0310eeac5f69480a75e2f01622e5b28378f&w=996'], nombre_personnes: 4, temps_preparation: 15, temps_cuisson: 10, temps_repos: 0})
CREATE (r2:Recipe {titre: 'Spaghetti Bolognese', origine: 'Italie', note: 4.8, total_notes: 15, somme_notes: 72, description: 'Spaghetti avec sauce bolognese traditionnelle.', images: ['https://img.freepik.com/photos-gratuite/composition-plat-pates-bolognaise_23-2148189891.jpg?t=st=1733178834~exp=1733182434~hmac=0063634d4e100da7c8a7680180cda5fc211141103530d2a1a64227ec4eb3e219&w=996'], nombre_personnes: 4, temps_preparation: 20, temps_cuisson: 30, temps_repos: 0})
CREATE (r3:Recipe {titre: 'Tarte aux pommes', origine: 'France', note: 4.7, total_notes: 12, somme_notes: 56, description: 'Tarte sucrée aux pommes avec pâte feuilletée.', images: ['https://img.freepik.com/photos-gratuite/delicieux-dessert-aux-pommes-angle-eleve_23-2149452284.jpg?t=st=1733178865~exp=1733182465~hmac=db519c40a1019c3602c7775b73e1fae731985aafda8c879e1f0b90ee7a380f05&w=1060'], nombre_personnes: 6, temps_preparation: 10, temps_cuisson: 40, temps_repos: 0})
CREATE (r4:Recipe {titre: 'Ratatouille', origine: 'France', note: 4.6, total_notes: 8, somme_notes: 37, description: 'Mélange de légumes de saison cuits à l\'huile d\'olive.', images: ['https://img.freepik.com/photos-gratuite/ratatouille-legumes-dans-poele-table-bois_2829-19906.jpg?t=st=1733178982~exp=1733182582~hmac=91be8af17b86d6852b0cbbad3d2d38dedc677d84fd676b7ea38dfd270cedef0b&w=1060'], nombre_personnes: 4, temps_preparation: 15, temps_cuisson: 45, temps_repos: 0})
CREATE (r5:Recipe {titre: 'Burger végétarien', origine: 'USA', note: 4.3, total_notes: 7, somme_notes: 30, description: 'Burger avec un steak de légumes, fromage et légumes frais.', images: ['https://img.freepik.com/photos-gratuite/delicieux-hamburgers-angle-eleve_23-2148575453.jpg?t=st=1733244631~exp=1733248231~hmac=ef82b46db34a17a7822206e7352411194ae195b2edf9262cca038ee202280562&w=1380'], nombre_personnes: 2, temps_preparation: 10, temps_cuisson: 5, temps_repos: 0})
CREATE (r6:Recipe {titre: 'Sushis', origine: 'Japon', note: 5, total_notes: 20, somme_notes: 100, description: 'Sushis traditionnels avec du poisson cru.', images: ['https://img.freepik.com/photos-gratuite/image-generee-par-ia-plaque-sushis_268835-6985.jpg?t=st=1733179092~exp=1733182692~hmac=9987d58829a772d97b95ef259b4af1d26f511220984a5391fa0c563301ff6b36&w=1060'], nombre_personnes: 2, temps_preparation: 30, temps_cuisson: 0, temps_repos: 0})
CREATE (r7:Recipe {titre: 'Paella', origine: 'Espagne', note: 4.9, total_notes: 18, somme_notes: 88, description: 'Paella traditionnelle avec fruits de mer et légumes.', images: ['https://img.freepik.com/photos-gratuite/vue-dessus-delicieuse-paella-aux-fruits-mer-rondelles-oignon_181624-29812.jpg?t=st=1733179058~exp=1733182658~hmac=752f6c784e41387e0e1fa31234ada152ef8f94878f8c54ab7cfb114adca91909&w=1060'], nombre_personnes: 6, temps_preparation: 20, temps_cuisson: 40, temps_repos: 0})
CREATE (r8:Recipe {titre: 'Moussaka', origine: 'Grèce', note: 4.4, total_notes: 10, somme_notes: 44, description: 'Gratin de légumes, viande hachée et béchamel.', images: ['https://img.freepik.com/photos-gratuite/plat-gratine-aubergines-crues-mozzarella-tomates_2829-19721.jpg?t=st=1733179189~exp=1733182789~hmac=60c8987c8d3b32b8af493fdaa7b17b7729d32a9133212a405940989a1a8fa9c7&w=1060'], nombre_personnes: 4, temps_preparation: 25, temps_cuisson: 50, temps_repos: 0})
CREATE (r9:Recipe {titre: 'Quiche Lorraine', origine: 'France', note: 4.8, total_notes: 16, somme_notes: 77, description: 'Quiche traditionnelle avec lardons et crème.', images: ['https://img-3.journaldesfemmes.fr/wwU6cIzA598kBoIiAe8-ls7fkQo=/750x500/8d6f0aff4d3c4e73ba36f441f35bf2ad/ccmcms-jdf/39977749.jpg'], nombre_personnes: 6, temps_preparation: 20, temps_cuisson: 40, temps_repos: 0})
CREATE (r10:Recipe {titre: 'Chili con carne', origine: 'Mexique', note: 4.6, total_notes: 14, somme_notes: 64, description: 'Plat épicé à base de viande hachée, haricots rouges et épices.', images: ['https://img-3.journaldesfemmes.fr/11HuCW8eTK6o78vfCy0ir9vqu6Q=/750x500/35cec2dae7e24d32aed06b57c66a6eed/ccmcms-jdf/39882596.jpg'], nombre_personnes: 4, temps_preparation: 15, temps_cuisson: 60, temps_repos: 0})

// Création des ingrédients
CREATE (i1:Ingredient {titre: 'Poulet', description: 'Viande de poulet grillée', prix: 5.99})
CREATE (i2:Ingredient {titre: 'Laitue Romaine', description: 'Salade verte croquante', prix: 2.50})
CREATE (i3:Ingredient {titre: 'Pâtes Spaghetti', description: 'Pâtes longues italiennes', prix: 1.99})
CREATE (i4:Ingredient {titre: 'Boeuf Haché', description: 'Viande de boeuf hachée', prix: 6.99})
CREATE (i5:Ingredient {titre: 'Pommes', description: 'Fruits sucrés', prix: 2.00})
CREATE (i6:Ingredient {titre: 'Poivrons', description: 'Légume sucré', prix: 1.50})
CREATE (i7:Ingredient {titre: 'Tomates', description: 'Légume rouge et juteux', prix: 2.20})
CREATE (i8:Ingredient {titre: 'Aubergines', description: 'Légume de saison pour ratatouille', prix: 1.80})
CREATE (i9:Ingredient {titre: 'Riz', description: 'Céréale cuite', prix: 3.50})
CREATE (i10:Ingredient {titre: 'Haricots rouges', description: 'Haricots utilisés dans le chili', prix: 2.00})

// Création des ustensiles
CREATE (u1:Utensil {titre: 'Poêle', description: 'Ustensile pour cuire des aliments', prix: 20.00})
CREATE (u2:Utensil {titre: 'Couteau', description: 'Ustensile de cuisine pour couper', prix: 10.00})
CREATE (u3:Utensil {titre: 'Plat à tarte', description: 'Ustensile utilisé pour cuire des tartes', prix: 15.50})
CREATE (u4:Utensil {titre: 'Mixeur', description: 'Ustensile pour mélanger des ingrédients', prix: 30.00})
CREATE (u5:Utensil {titre: 'Casserole', description: 'Ustensile pour cuire des liquides', prix: 25.00})
CREATE (u6:Utensil {titre: 'Fouet', description: 'Ustensile pour mélanger des ingrédients', prix: 8.50})
CREATE (u7:Utensil {titre: 'Four', description: 'Appareil pour cuire des aliments', prix: 150.00})
CREATE (u8:Utensil {titre: 'Grill', description: 'Ustensile pour cuire à la chaleur directe', prix: 60.00})
CREATE (u9:Utensil {titre: 'Marmite', description: 'Grand récipient pour cuire des plats', prix: 40.00})
CREATE (u10:Utensil {titre: 'Couteau à pain', description: 'Couteau utilisé pour couper le pain', prix: 12.00})

// Relations entre les recettes et les catégories
CREATE (r1)-[:APPARTIENT_A]->(cat1)
CREATE (r1)-[:APPARTIENT_A]->(cat4)

CREATE (r2)-[:APPARTIENT_A]->(cat2)

CREATE (r3)-[:APPARTIENT_A]->(cat3)
CREATE (r3)-[:APPARTIENT_A]->(cat5)

CREATE (r4)-[:APPARTIENT_A]->(cat2)
CREATE (r4)-[:APPARTIENT_A]->(cat4)

CREATE (r5)-[:APPARTIENT_A]->(cat2)
CREATE (r5)-[:APPARTIENT_A]->(cat4)

CREATE (r6)-[:APPARTIENT_A]->(cat7)

CREATE (r7)-[:APPARTIENT_A]->(cat2)
CREATE (r7)-[:APPARTIENT_A]->(cat8)

CREATE (r8)-[:APPARTIENT_A]->(cat2)
CREATE (r8)-[:APPARTIENT_A]->(cat8)

CREATE (r9)-[:APPARTIENT_A]->(cat2)
CREATE (r9)-[:APPARTIENT_A]->(cat3)

CREATE (r10)-[:APPARTIENT_A]->(cat2)
CREATE (r10)-[:APPARTIENT_A]->(cat6)


// Relations entre les recettes et les ingrédients
CREATE (r1)-[:CONTIENT {quantite: 200, type_unite: 'g'}]->(i1)
CREATE (r1)-[:CONTIENT {quantite: 150, type_unite: 'g'}]->(i2)

CREATE (r2)-[:CONTIENT {quantite: 250, type_unite: 'g'}]->(i3)
CREATE (r2)-[:CONTIENT {quantite: 300, type_unite: 'g'}]->(i4)

CREATE (r3)-[:CONTIENT {quantite: 500, type_unite: 'g'}]->(i5)
CREATE (r3)-[:CONTIENT {quantite: 200, type_unite: 'g'}]->(i3)

CREATE (r4)-[:CONTIENT {quantite: 200, type_unite: 'g'}]->(i6)
CREATE (r4)-[:CONTIENT {quantite: 200, type_unite: 'g'}]->(i7)
CREATE (r4)-[:CONTIENT {quantite: 300, type_unite: 'g'}]->(i8)

CREATE (r5)-[:CONTIENT {quantite: 150, type_unite: 'g'}]->(i9)
CREATE (r5)-[:CONTIENT {quantite: 100, type_unite: 'g'}]->(i6)
CREATE (r5)-[:CONTIENT {quantite: 200, type_unite: 'g'}]->(i8)

CREATE (r6)-[:CONTIENT {quantite: 100, type_unite: 'g'}]->(i4)
CREATE (r6)-[:CONTIENT {quantite: 50, type_unite: 'g'}]->(i10)

CREATE (r7)-[:CONTIENT {quantite: 150, type_unite: 'g'}]->(i6)
CREATE (r7)-[:CONTIENT {quantite: 400, type_unite: 'g'}]->(i9)

CREATE (r8)-[:CONTIENT {quantite: 300, type_unite: 'g'}]->(i7)
CREATE (r8)-[:CONTIENT {quantite: 250, type_unite: 'g'}]->(i4)

CREATE (r9)-[:CONTIENT {quantite: 100, type_unite: 'g'}]->(i6)
CREATE (r9)-[:CONTIENT {quantite: 200, type_unite: 'g'}]->(i5)

CREATE (r10)-[:CONTIENT {quantite: 250, type_unite: 'g'}]->(i10)
CREATE (r10)-[:CONTIENT {quantite: 200, type_unite: 'g'}]->(i8)


// Relations entre les recettes et les ustensiles
CREATE (r1)-[:UTILISE {nombre: 1}]->(u2)
CREATE (r1)-[:UTILISE {nombre: 1}]->(u4)

CREATE (r2)-[:UTILISE {nombre: 1}]->(u5)
CREATE (r2)-[:UTILISE {nombre: 1}]->(u1)

CREATE (r3)-[:UTILISE {nombre: 1}]->(u3)
CREATE (r3)-[:UTILISE {nombre: 1}]->(u5)

CREATE (r4)-[:UTILISE {nombre: 1}]->(u5)
CREATE (r4)-[:UTILISE {nombre: 1}]->(u7)

CREATE (r5)-[:UTILISE {nombre: 1}]->(u2)
CREATE (r5)-[:UTILISE {nombre: 1}]->(u4)

CREATE (r6)-[:UTILISE {nombre: 1}]->(u6)
CREATE (r6)-[:UTILISE {nombre: 1}]->(u10)

CREATE (r7)-[:UTILISE {nombre: 1}]->(u9)
CREATE (r7)-[:UTILISE {nombre: 1}]->(u8)

CREATE (r8)-[:UTILISE {nombre: 1}]->(u3)
CREATE (r8)-[:UTILISE {nombre: 1}]->(u7)

CREATE (r9)-[:UTILISE {nombre: 1}]->(u5)
CREATE (r9)-[:UTILISE {nombre: 1}]->(u4)

CREATE (r10)-[:UTILISE {nombre: 1}]->(u9)
CREATE (r10)-[:UTILISE {nombre: 1}]->(u1)

// Création des commentaires pour chaque recette
CREATE (c1:Comments {uuid: 'c1', texte: 'Délicieuse recette, très facile à réaliser.', note: 5})
CREATE (c2:Comments {uuid: 'c2', texte: 'Parfait pour un dîner rapide. Merci !', note: 4})
CREATE (c3:Comments {uuid: 'c3', texte: 'J\'ai remplacé le poulet par des crevettes, c\'était délicieux.', note: 5})

CREATE (c4:Comments {uuid: 'c4', texte: 'Authentique et savoureuse.', note: 5})
CREATE (c5:Comments {uuid: 'c5', texte: 'Trop long à préparer, mais le résultat est bon.', note: 3})
CREATE (c6:Comments {uuid: 'c6', texte: 'Un classique qui ne déçoit jamais.', note: 4})

CREATE (c7:Comments {uuid: 'c7', texte: 'Parfait dessert pour la famille.', note: 5})
CREATE (c8:Comments {uuid: 'c8', texte: 'Pâte croustillante et pommes bien fondantes.', note: 4})
CREATE (c9:Comments {uuid: 'c9', texte: 'Manque un peu de sucre pour mon goût.', note: 3})

CREATE (c10:Comments {uuid: 'c10', texte: 'Rien à redire, c\'est délicieux.', note: 5})
CREATE (c11:Comments {uuid: 'c11', texte: 'Un peu trop d\'huile pour moi.', note: 3})
CREATE (c12:Comments {uuid: 'c12', texte: 'Simple et efficace.', note: 4})

CREATE (c13:Comments {uuid: 'c13', texte: 'Excellente alternative végétarienne.', note: 5})
CREATE (c14:Comments {uuid: 'c14', texte: 'Le pain était un peu trop sec.', note: 3})
CREATE (c15:Comments {uuid: 'c15', texte: 'Légèrement fade, j\'ai ajouté des épices.', note: 4})

CREATE (c16:Comments {uuid: 'c16', texte: 'Rafraîchissant et délicieux.', note: 5})
CREATE (c17:Comments {uuid: 'c17', texte: 'J\'ai utilisé du saumon au lieu du thon, parfait.', note: 4})
CREATE (c18:Comments {uuid: 'c18', texte: 'Trop difficile à préparer pour un débutant.', note: 3})

CREATE (c19:Comments {uuid: 'c19', texte: 'Un plat complet et savoureux.', note: 5})
CREATE (c20:Comments {uuid: 'c20', texte: 'Les fruits de mer étaient trop cuits.', note: 3})
CREATE (c21:Comments {uuid: 'c21', texte: 'Un vrai goût d\'Espagne.', note: 4})

CREATE (c22:Comments {uuid: 'c22', texte: 'Parfait équilibre de saveurs.', note: 5})
CREATE (c23:Comments {uuid: 'c23', texte: 'Un peu trop gras à mon goût.', note: 3})
CREATE (c24:Comments {uuid: 'c24', texte: 'Bonne recette, mais pas exceptionnelle.', note: 4})

CREATE (c25:Comments {uuid: 'c25', texte: 'Idéal pour un brunch.', note: 5})
CREATE (c26:Comments {uuid: 'c26', texte: 'Manque un peu de garniture.', note: 3})
CREATE (c27:Comments {uuid: 'c27', texte: 'Facile à préparer et délicieux.', note: 4})

CREATE (c28:Comments {uuid: 'c28', texte: 'Excellente recette épicée.', note: 5})
CREATE (c29:Comments {uuid: 'c29', texte: 'Les haricots étaient un peu trop fermes.', note: 3})
CREATE (c30:Comments {uuid: 'c30', texte: 'Un plat très réconfortant.', note: 4})

// Ajout des relations entre les recettes et leurs commentaires
CREATE (r1)-[:POSSEDE]->(c1)
CREATE (r1)-[:POSSEDE]->(c2)
CREATE (r1)-[:POSSEDE]->(c3)

CREATE (r2)-[:POSSEDE]->(c4)
CREATE (r2)-[:POSSEDE]->(c5)
CREATE (r2)-[:POSSEDE]->(c6)

CREATE (r3)-[:POSSEDE]->(c7)
CREATE (r3)-[:POSSEDE]->(c8)
CREATE (r3)-[:POSSEDE]->(c9)

CREATE (r4)-[:POSSEDE]->(c10)
CREATE (r4)-[:POSSEDE]->(c11)
CREATE (r4)-[:POSSEDE]->(c12)

CREATE (r5)-[:POSSEDE]->(c13)
CREATE (r5)-[:POSSEDE]->(c14)
CREATE (r5)-[:POSSEDE]->(c15)

CREATE (r6)-[:POSSEDE]->(c16)
CREATE (r6)-[:POSSEDE]->(c17)
CREATE (r6)-[:POSSEDE]->(c18)

CREATE (r7)-[:POSSEDE]->(c19)
CREATE (r7)-[:POSSEDE]->(c20)
CREATE (r7)-[:POSSEDE]->(c21)

CREATE (r8)-[:POSSEDE]->(c22)
CREATE (r8)-[:POSSEDE]->(c23)
CREATE (r8)-[:POSSEDE]->(c24)

CREATE (r9)-[:POSSEDE]->(c25)
CREATE (r9)-[:POSSEDE]->(c26)
CREATE (r9)-[:POSSEDE]->(c27)

CREATE (r10)-[:POSSEDE]->(c28)
CREATE (r10)-[:POSSEDE]->(c29)
CREATE (r10)-[:POSSEDE]->(c30)
