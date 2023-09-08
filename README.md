# README
## Description du Projet

Ce projet est une application Python qui utilise l'Intelligence Artificielle pour analyser et répondre à des questions en français. Il s'appuie sur l'API OpenAI pour générer des réponses basées sur le contenu web récupéré à partir d'une question donnée.

## Installation

Pour installer ce projet, suivez les étapes suivantes :

1. Clonez ce dépôt sur votre machine locale.
2. Installez les dépendances nécessaires en utilisant pip :

```bash
pip install -r requirements.txt
```

## Configuration

Pour configurer ce projet, vous devez créer un fichier .env à la racine du projet et y ajouter les variables d'environnement suivantes :

- FILE_EMBEDING : Le chemin vers le fichier d'embedding.
- OPENAI_API_KEY : Votre clé API OpenAI.

et dans main.py :

- VERBOSE : Un booléen qui détermine si le programme doit afficher des messages de débogage.
- QUESTION : La question que vous voulez poser au programme.
- NUM_LINK : Le nombre de liens à récupérer lors de la recherche d'informations sur le web.
Utilisation

Pour utiliser ce projet, exécutez le fichier main.py avec Python :

```bash
python main.py
```

Le programme vous demandera une question en français et cherchera ensuite des informations sur le web pour répondre à votre question.
Fonctionnalités Principales

- get_webpage_text(url) : Récupère le texte d'une page web à partir de son URL.
- analyze_text(prompt) : Analyse le texte et génère une réponse à l'aide de l'IA.
- multi_traitement_ressource(prompt, data) : Traite plusieurs ressources et génère une réponse.
- clean_url(url) : Nettoie une URL pour enlever les caractères indésirables.
- web_qa(url_list, query) : Récupère le contenu de plusieurs URLs et génère une réponse à une question.
- trouver_urls(texte) : Trouve toutes les URLs dans un texte.
- main() : Fonction principale qui exécute le programme.
Contribution

Les contributions sont les bienvenues. Veuillez créer une issue pour discuter des modifications proposées avant de faire une pull request.
Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
