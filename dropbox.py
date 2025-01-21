import dropbox

# Votre clé API à durée limitée
DROPBOX_API_KEY = "SL.BWQsdpPKqw1Q7Fb3pQ=eEQ_b4Glzxtw2L_LUVlzr8oAqPEefvwAEjBſiTs4Qfzy9xxTw02quvaKf2xgQzT94163ſo6QlQQh-j15KEKzAV9JH7YJUgQMtB9DFTUws1XTZi7sEwZs"

# Initialisation de Dropbox
dbx = dropbox.Dropbox(DROPBOX_API_KEY)

def upload_file(file_path, dropbox_path):
    """Télécharge un fichier sur Dropbox."""
    with open(file_path, "rb") as f:
        dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)
    print(f"Fichier '{file_path}' téléchargé sur '{dropbox_path}'.")

def create_shared_link(dropbox_path):
    """Crée un lien de partage pour un fichier sur Dropbox."""
    link = dbx.sharing_create_shared_link_with_settings(dropbox_path)
    print(f"Lien de partage : {link.url}")

# Exemple d'utilisation
if __name__ == "__main__":
    local_file = "test.txt"          # Chemin local du fichier à uploader
    dropbox_file_path = "/test.txt" # Chemin sur Dropbox

    try:
        # Télécharger le fichier
        upload_file(local_file, dropbox_file_path)
        # Créer un lien de partage
        create_shared_link(dropbox_file_path)
    except dropbox.exceptions.AuthError as e:
        print(f"Erreur d'authentification : {e}")
    except Exception as e:
        print(f"Erreur : {e}")