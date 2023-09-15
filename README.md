# README RECHERCHE WEB

## Description

Ce projet utilise un modèle de langage pour répondre aux questions basées sur des ressources Web et des documents locaux. Il utilise l'API OpenAI pour générer des réponses et effectuer des recherches sur le web.

## Scripts

### demonstration.py

- **Fonctionnalité** : Exécute le moteur principal pour obtenir une réponse basée sur une entrée utilisateur.
- **Dépendances** : `Moteur_du_tool`, `dotenv`, `os`, `json`

### Moteur_du_jeux.py

- **Fonctionnalité** : Contient toutes les fonctions nécessaires pour interagir avec le web, analyser le texte, et interagir avec l'API OpenAI.
- **Dépendances** : `langchain`, `BeautifulSoup`, `dotenv`, `requests`, `re`, `openai`

## Configuration

Un fichier `.env` est nécessaire pour configurer les variables d'environnement utilisées par les scripts. Les variables à définir sont :

- `FILE_EMBEDING`: Chemin vers le fichier de ressources.
- `OPENAI_API_KEY`: Clé API pour OpenAI.
- `input_user`: Question ou entrée utilisateur.
- `model`: Modèle OpenAI à utiliser.

## Installation

Pour installer les dépendances nécessaires, exécutez :

```bash
pip install -r requirements.txt
```

## Utilisation

1. Configurez le fichier `.env` avec les bonnes valeurs.
2. Exécutez `demonstration.py` pour obtenir une réponse basée sur l'entrée utilisateur.

## Exemple d'input

 - Qui est le pere de eren dans snk ?
 - de quoi parle cette page https://python.langchain.com/docs/use_cases/chatbots ?
