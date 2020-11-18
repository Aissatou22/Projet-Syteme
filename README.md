# Projet-Syteme
Creation d’une Application Client / Serveur avec Python pour permettre aux clients de consulter leurs factures d'électricité

SERVEURS :

serveurFlask.py : renvoie les lignes des pages Wikipedia qui contiennent le paramètre
                  pour l'invoquer à partir du terminal : curl localhost:5000/recherche/<parametre>

serveurFlask_1.py : renvoie en plus de la ligne, le nom de la page Wikipedia d'où elle a été extraite
                    pour éviter des problèmes de CORS :
                    - peut renvoyer recherche.html sur la route /recherche
                    - peut renvoyer recherche_1.html sur la route /recherche_1

-----------------------------------------------------------------------------------------------------------
CLIENTS :

recherche.py : appel de serveurFlask.py avec le paramètre recherché

recherche_1.py : renvoie le nom de la page en plus du contenu de la ligne (appel de serveurFlask_1.py)

recherche.html : formulaire de recherche, les résultats s'affichent dans la console du navigateur (appel de serveurFlask_1.py)
                 cette page peut être chargée à partir du serveur : localhost:5000/recherche

recherche_1.html : formulaire de recherche, les résultats sont intégrés dans la page (appel de serveurFlask_1.py)
                 cette page peut être chargée à partir du serveur : localhost:5000/recherche_1
