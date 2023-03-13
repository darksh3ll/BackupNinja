# Backup Ninja

![Nom de l'image](logo.png)


# Script de sauvegarde de dossier avec Rsync

Ce script Python utilise la commande Rsync pour sauvegarder des dossiers et leurs contenus. Vous pouvez spécifier les dossiers que vous souhaitez sauvegarder ainsi que les destinations de sauvegarde pour chacun d'entre eux. Il existe deux versions du script : 

incremental_backup.py et versionned_backup.py.

* **incremental_backup.py** effectue une sauvegarde incrémentielle des dossiers sélectionnés. Cette version compare les fichiers et les dossiers source avec les fichiers et dossiers existants dans la destination de sauvegarde, puis ne sauvegarde que les fichiers et les dossiers qui ont été modifiés ou ajoutés depuis la dernière sauvegarde.

----


* **versionned_backup.py** versionne les sauvegardes des dossiers sélectionnés en créant un dossier pour chaque sauvegarde qui inclut la date et l'heure de la sauvegarde. Cette version permet de conserver un historique de sauvegardes et de récupérer des versions précédentes de fichiers ou de dossiers.

Ce script est intéressant pour plusieurs raisons :

Il permet de sauvegarder des dossiers et leurs contenus de manière efficace. La commande Rsync est une méthode rapide et fiable pour sauvegarder des données, car elle ne transfère que les fichiers modifiés ou ajoutés depuis la dernière sauvegarde.

Il est facile à utiliser et à configurer. Vous pouvez spécifier les dossiers que vous souhaitez sauvegarder ainsi que les destinations de sauvegarde pour chacun d'entre eux. De plus, il est possible de personnaliser les exclusions de fichiers ou de dossiers à partir de la liste exclude_dirs.

Il offre deux options pour la sauvegarde : une sauvegarde incrémentielle ou une sauvegarde versionnée. La version incrémentielle permet de sauvegarder uniquement les modifications apportées depuis la dernière sauvegarde, tandis que la version versionnée conserve un historique de sauvegardes pour permettre une récupération facile de fichiers ou de dossiers antérieurs.


# Dépendances

1. Python 3.x
2. Rsync doit être installé sur votre système

# Utilisation

Clonez ce dépôt Git ou téléchargez le fichier backup_script.py.

Modifiez les variables USER et IP_SERVER pour correspondre à votre nom d'utilisateur et à l'adresse IP de votre serveur de sauvegarde.

    USER = ''
    IP_SERVER = ""`

Ajoutez les dossiers que vous souhaitez sauvegarder et les destinations de sauvegarde dans la liste dossiers en utilisant la structure suivante :

```
dossiers = [
    {
        "source": "/chemin/vers/le/dossier/source",
        "destinations": [
            "utilisateur@serveur:/chemin/vers/la/destination/",
            "utilisateur@serveur:/chemin/vers/une/autre/destination/"
        ]
    },
    {
        "source": "/chemin/vers/un/autre/dossier/source",
        "destinations": [
            "utilisateur@serveur:/chemin/vers/la/destination/"
        ]
    }
]

```
Exécutez le script à l'aide de la commande suivante:

`python incremental_backup.py`

# Fonctionnement

* Le script vérifie si l'adresse IP du serveur de sauvegarde est valide.
* Le script boucle à travers chaque dossier spécifié dans la liste dossiers.
* Pour chaque dossier, le script obtient le chemin du dossier source, le nom du dossier et la liste des destinations de sauvegarde.
* Le script exclut certains dossiers qui ne sont pas nécessaires à sauvegarder, tels que les dossiers node_modules, env, venv et __pycache__.
* Le script exécute la commande de sauvegarde avec rsync et affiche une barre de progression à l'aide de la bibliothèque tqdm.
* Si une erreur se produit pendant la sauvegarde, le script affiche un message d'erreur correspondant.
* Si une erreur réseau se produit, le script affiche un message d'erreur correspondant.
* Si une destination n'est pas valide, le script affiche un message d'erreur correspondant.
* N'oubliez pas que ce script est fourni tel quel et sans garantie. Vous êtes responsable de l'utilisation de ce script et de toute perte de données qui pourrait en résulter.

# Licence

Ce script est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

# Contribuer

Les contributions sont les bienvenues ! Si vous avez des idées pour améliorer ce script ou si vous avez trouvé un bogue, veuillez ouvrir une issue ou soumettre une pull request.