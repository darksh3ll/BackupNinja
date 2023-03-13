  # try:
    #     # Exclure certains dossiers qui ne sont pas nécessaires à sauvegarder
    #     exclude_dirs = ['node_modules', 'env', 'venv', '__pycache__']
    #     exclude_options = [f'--exclude={dir}' for dir in exclude_dirs]

    #     # Exécuter la commande de sauvegarde avec rsync
    #     rsync_command = ['rsync', '-avh'] + exclude_options + ['--update', source_dir, destination_dir]
    #     subprocess.run(rsync_command, check=True)

    # # Si une erreur se produit, afficher un message d'erreur
    # except subprocess.CalledProcessError:
    #     print(f"Error during backup of {source_dir}")

    # # Si une erreur réseau se produit, afficher un message d'erreur
    # except OSError:
    #     print("Network error. Check your network connection.")

    # # Si la destination n'est pas valide, afficher un message d'erreur
    # except ValueError:
    #     print(f"Invalid destination: {destination_dir}")
