# AI Words Generator

AI Words Generator est un script Python qui utilise l'API OpenAI pour générer du contenu basé sur des prompts personnalisés. Ce script gère jusqu'à 4 clés API pour un usage optimisé.

## 🚀 Installation

1. **Clonez le dépôt :**
   ```bash
   git clone https://github.com/tucommenceapousser/aiwordsgen.git
   cd aiwordsgen
   ```

2. **Installez les dépendances nécessaires :**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurez vos clés API OpenAI :**
   - Créez un fichier `.env` dans le répertoire racine :
     ```bash
     touch .env
     ```
   - Ajoutez-y vos 4 clés OpenAI en suivant ce format :
     ```
     OPENAI=Votre_Cle_OpenAI
     OPENAI1=Votre_Cle_OpenAI1
     OPENAI2=Votre_Cle_OpenAI2
     OPENAI3=Votre_Cle_OpenAI3
     ```

4. **Testez l'installation :**
   ```bash
   python main.py
   ```

## 📖 Utilisation

1. **Exécution du script :**
   - Lancez le script pour générer du contenu :
     ```bash
     python main.py
     ```

2. **Prompts personnalisés :**
   - Lors de l'exécution, vous serez invité à saisir divers détails (prénom, nom, mot fétiche, etc.) pour générer une liste de mots contextualisés.

3. **Sauvegarde de la wordlist :**
   - Le script génère et enregistre la liste des mots dans un fichier spécifié.

## 🛠️ Dépendances

- Python 3.7 ou supérieur
- `openai`
- `python-dotenv`
- `questionary`

## 🧑‍💻 Contribution

Les contributions sont les bienvenues ! Pour toute suggestion ou amélioration, n'hésitez pas à créer une issue ou à soumettre une pull request.

## 🛡️ Licence

Ce projet est sous licence [MIT](LICENSE).(LICENSE).