import requests
from bs4 import BeautifulSoup
import questionary
import openai
from datetime import datetime
from itertools import permutations
import os

openai.api_key = os.environ["OPENAI"]
# Headers pour scraping
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def calculate_age(birth_date):
    """Calcule l'âge basé sur la date de naissance."""
    try:
        birth_year = int(birth_date.split()[-1])
        current_year = datetime.now().year
        return current_year - birth_year
    except:
        return None

def scrape_facebook_profile(profile_url):
    """Scrape les informations d'un profil Facebook."""
    try:
        response = requests.get(profile_url, headers=HEADERS)
        if response.status_code != 200:
            print(f"❌ Échec du scraping : Code {response.status_code}")
            return None

        soup = BeautifulSoup(response.content, "html.parser")

        # Extraction des données basiques
        name = soup.find("title").text.strip()
        bio_section = soup.find("div", {"id": "bio"})
        bio = bio_section.text.strip() if bio_section else ""

        birth_date = None
        for text in soup.stripped_strings:
            if "né le" in text or "anniversaire" in text.lower():
                birth_date = text.strip()
                break

        return {
            "name": name,
            "bio": bio,
            "birth_date": birth_date
        }
    except Exception as e:
        print(f"Erreur : {e}")
        return None

def generate_wordlist_with_context(profile_data, region_language):
    """Génère une wordlist enrichie avec contexte."""
    base_words = [profile_data.get("name", ""), profile_data.get("bio", "")]
    birth_date = profile_data.get("birth_date", "")
    age = calculate_age(birth_date)

    if age:
        print(f"🔢 Âge estimé : {age} ans")
        base_words.append(f"{age}ans")

    # Ajout de mots basés sur la région/l'âge
    region_words = {
        "fr": ["bonjour", "amour", "chat", "famille", "amitié", "secret"],
        "en": ["hello", "love", "friend", "secret", "family", "birthday"],
        "es": ["hola", "amor", "familia", "secreto", "cumpleaños", "amigos"]
    }
    base_words.extend(region_words.get(region_language, []))

    # Génération basique de permutations
    permutations_list = [''.join(p) for p in permutations(base_words, 2)]
    wordlist = set(base_words + permutations_list)

    return wordlist

def enhance_with_gpt4(base_words, age, region_language):
    """Utilise GPT-4 pour enrichir avec lexique et variations spécifiques."""
    prompt = (
        f"Voici une liste de mots liés à une personne de {age} ans, "
        f"parlant {region_language}, avec un contexte générationnel et régional : "
        f"{', '.join(base_words)}. "
        "Génère des mots de passe probables en combinant ces mots, ajoutant des substitutions courantes "
        "(comme @ pour a, 3 pour e), et en tenant compte du lexique de cette langue. "
        "Crée des mots réalistes et variés, entre 6 et 12 caractères."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=300
        )
        suggestions = response['choices'][0]['message']['content'].splitlines()
        return [s.strip() for s in suggestions if len(s.strip()) >= 6]
    except Exception as e:
        print(f"Erreur avec GPT-4 : {e}")
        return []

def main():
    print("\n=== Générateur de Wordlist Contextuel ===\n")

    # Collecter les informations
    profile_url = questionary.text("Entrez l'URL du profil Facebook public :").ask()
    region_language = questionary.select(
        "Choisissez la langue ou région :",
        choices=["fr", "en", "es", "autre"]
    ).ask()

    # Scraper le profil
    profile_data = scrape_facebook_profile(profile_url)
    if not profile_data:
        print("❌ Échec du scraping. Assurez-vous que l'URL est correcte.")
        return

    # Afficher les informations extraites
    print("\n🔍 Informations extraites :")
    for key, value in profile_data.items():
        print(f"- {key.capitalize()} : {value}")

    # Génération de la wordlist
    print("\n🔄 Génération de la wordlist de base...")
    wordlist = generate_wordlist_with_context(profile_data, region_language)

    # Enrichir avec GPT-4
    age = calculate_age(profile_data.get("birth_date", ""))
    print("\n🔄 Enrichissement avec GPT-4...")
    gpt4_suggestions = enhance_with_gpt4(list(wordlist), age, region_language)
    wordlist.update(gpt4_suggestions)

    # Sauvegarder la wordlist
    file_name = questionary.text("Nom du fichier pour sauvegarder la wordlist :").ask()
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    with open(file_name, "w") as f:
        for word in sorted(wordlist):
            f.write(word + "\n")

    print(f"\n✅ Wordlist générée avec {len(wordlist)} mots et sauvegardée dans {file_name} !")

if __name__ == "__main__":
    main()