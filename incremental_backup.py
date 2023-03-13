import subprocess
import socket

# -----------------------------------------------------------
# Définir les informations de l'utilisateur et du serveur SSH
# -----------------------------------------------------------
USER = 'darksh3ll'
IP_SERVER = ''

# -----------------------------------------------------------
# Définir le nom identifiant de la sauvegarde
# Attention antislash obligatoire
# -----------------------------------------------------------
backup_folder_name = 'backup/'

# -----------------------------------------------------------
# Définir la liste des dossiers à sauvegarder et les destinations de sauvegarde
# "source" => dossier a sauvegarder
# "destination" => sauvegarde dossier source
# -----------------------------------------------------------

dossiers = [
    {
        "source": "/Users/darksh3ll/Desktop/Fritzing-Library-master/",
        "destinations": [
            # f"{USER}@{IP_SERVER}://srv/dev-disk-by-uuid-1b8845f0-16ce-4574-98dc-e0ec5029c1a9/time_machine/",
            "/Volumes/data/",
        ]
    },
    {
        "source": "/Users/darksh3ll/Desktop/rsync",
        "destinations": [
            # f"{USER}@{IP_SERVER}://srv/dev-disk-by-uuid-1b8845f0-16ce-4574-98dc-e0ec5029c1a9/time_machine/",
            "/Volumes/data/",
        ]
    },
]


# -----------------------------------------------------------
# Code ne pas modifier ❌
# -----------------------------------------------------------

def test_ping(ip_address):
    """
    Teste si une adresse IP est active en envoyant une requête ping.
    Retourne True si l'adresse est active, False sinon.
    """
    try:
        output = subprocess.check_output(['ping', '-c', '1', ip_address])
        if '1 received' in output.decode('utf-8'):
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False


# Vérifier si l'adresse IP est valide et active
if IP_SERVER and IP_SERVER.strip():
    try:
        socket.inet_aton(IP_SERVER)
        if not test_ping(IP_SERVER):
            print(f"L'adresse IP {IP_SERVER} ne répond pas. Fermeture...")
            exit()
    except socket.error:
        print(f"Invalid IP address: {IP_SERVER}")
        exit()

# Boucle à travers chaque dossier à sauvegarder
for dossier in dossiers:
    # Obtenir le chemin du dossier source et la liste des destinations
    source_dir = dossier['source']
    destinations = dossier['destinations']

    # Vérifier si le chemin du dossier source se termine par un "/"
    if not source_dir.endswith('/'):
        source_dir += '/'

    print("source", source_dir)
    # Obtenir le nom du dossier à partir du chemin du dossier source
    folder_name = source_dir.split('/')[-2]

    # Obtenir le chemin du dossier de sauvegarde
    destination_dir = ''
    for destination in destinations:
        if not destination.endswith('/'):
            destination += '/'
        destination_dir = f"{destination}{folder_name}_{backup_folder_name}"
        break

    if not destination_dir:
        continue

    try:
        # Exclure certains dossiers qui ne sont pas nécessaires à sauvegarder
        exclude_dirs = ['node_modules', 'env', 'venv', '__pycache__']
        exclude_options = [f'--exclude={dir}' for dir in exclude_dirs]

        # Exécuter la commande de sauvegarde avec rsync
        rsync_command = ['rsync', '-avh'] + exclude_options + ['--update', source_dir, destination_dir]
        subprocess.run(rsync_command, check=True)

    # Si une erreur se produit, afficher un message d'erreur
    except subprocess.CalledProcessError:
        print(f"Error during backup of {source_dir}")

    # Si une erreur réseau se produit, afficher un message d'erreur
    except OSError:
        print("Network error. Check your network connection.")

    # Si la destination n'est pas valide, afficher un message d'erreur
    except ValueError:
        print(f"Invalid destination: {destination_dir}")
