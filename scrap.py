import requests
from bs4 import BeautifulSoup
import questionary
import openai
from itertools import permutations, product
import re
import os

# Configurer votre clé OpenAI
openai.api_key = os.environ["OPENAI"]


# User-Agent pour éviter les blocages lors du scraping
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def scrape_facebook_profile(profile_url):
    """Scrape un profil Facebook public pour récupérer des informations utiles."""
    try:
        print(f"🔍 Scraping du profil : {profile_url}")
        response = requests.get(profile_url, headers=HEADERS)
        if response.status_code != 200:
            print(f"❌ Échec du scraping : Code {response.status_code}")
            return None

        soup = BeautifulSoup(response.content, "html.parser")

        # Extraction des informations basiques
        name = soup.find("title").text.strip()  # Le nom est souvent dans le titre
        bio_section = soup.find("div", {"id": "bio"})
        bio = bio_section.text.strip() if bio_section else ""

        # Recherche de l'anniversaire
        birth_date = None
        for text in soup.stripped_strings:
            if re.search(r"\b(?:né le|anniversaire)\b", text, re.IGNORECASE):
                birth_date = text
                break

        # Extraction des amis (exemple simplifié)
        friends_section = soup.find("div", text=re.compile(r"^Amis"))
        friends = friends_section.text.strip() if friends_section else ""

        return {
            "name": name,
            "bio": bio,
            "birth_date": birth_date,
            "friends": friends
        }

    except Exception as e:
        print(f"Erreur lors du scraping : {e}")
        return None

def generate_wordlist(details, min_length=6, max_length=12):
    """Génère une wordlist basée sur les informations extraites."""
    base_words = [
        details.get("name", ""),
        details.get("bio", ""),
        details.get("birth_date", ""),
        details.get("friends", ""),
    ]

    # Nettoyage et suppression des doublons
    base_words = list(set(filter(None, base_words)))

    wordlist = set()

    # Ajouter des mots simples
    for word in base_words:
        if min_length <= len(word) <= max_length:
            wordlist.add(word)

    # Ajouter des combinaisons
    for length in range(2, len(base_words) + 1):
        for combo in permutations(base_words, length):
            combined_word = ''.join(combo)
            if min_length <= len(combined_word) <= max_length:
                wordlist.add(combined_word)

    return wordlist

def enhance_with_gpt4(base_words):
    """Utilise GPT-4 pour enrichir les suggestions."""
    prompt = (
        "Voici une liste de mots : "
        f"{', '.join(base_words)}. "
        "Génère des variantes et des mots de passe probables en combinant ces mots, "
        "ajoutant des caractères spéciaux et des substitutions courantes comme @ pour a, 3 pour e, etc. "
        "Rends les mots de passe réalistes mais variés, avec des longueurs comprises entre 6 et 12 caractères."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=200
        )
        suggestions = response['choices'][0]['message']['content'].splitlines()
        return [s.strip() for s in suggestions if len(s.strip()) >= 6]
    except Exception as e:
        print(f"Erreur avec GPT-4 : {e}")
        return []

def main():
    print("\n=== Générateur de Wordlist avec Scraping et GPT-4 ===\n")

    # Collecter l'URL du profil Facebook
    profile_url = questionary.text("Entrez l'URL du profil Facebook public :").ask()

    # Scraper les informations du profil
    profile_details = scrape_facebook_profile(profile_url)
    if not profile_details:
        print("❌ Échec du scraping. Assurez-vous que l'URL est correcte et que le profil est public.")
        return

    print("\n🔍 Informations extraites :")
    for key, value in profile_details.items():
        print(f"- {key.capitalize()} : {value}")

    # Générer une wordlist de base
    print("\n🔄 Génération de la wordlist de base...")
    wordlist = generate_wordlist(profile_details)

    # Enrichir la wordlist avec GPT-4
    print("\n🔄 Enrichissement avec GPT-4...")
    gpt4_suggestions = enhance_with_gpt4(list(wordlist))
    wordlist.update(gpt4_suggestions)

    # Sauvegarder la wordlist dans un fichier
    file_name = questionary.text("Nom du fichier pour sauvegarder la wordlist :").ask()
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    with open(file_name, "w") as f:
        for word in sorted(wordlist):
            f.write(word + "\n")

    print(f"\n✅ Wordlist générée avec {len(wordlist)} mots et sauvegardée dans {file_name} !")

if __name__ == "__main__":
    main()