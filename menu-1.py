## Exemple de Stackoverflow:  https://stackoverflow.com/questions/75220524/python-cli-menu-with-arrow-keys-on-windows
# Avec ajout RCLONE

import subprocess
""" import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) """

from InquirerPy import inquirer  # Import the inquirer module
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
#from rclone_python import rclone  # Import the rclone module  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import logging  ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#logging.basicConfig(filename="fichier.log", level=logging.DEBUG)

## Paramétrage des logs -------------------------
from logging.handlers import RotatingFileHandler
logging.basicConfig(filename='log/programlog.log', level=logging.DEBUG, encoding='utf-8', format=' %(asctime)s - %(levelname)s -  %(message)s')

from rclone_python import rclone  # Import the rclone module

logger = logging.getLogger(__name__)  # LOG:

from icecream import ic # Outil de debug
## Paramétrage d'icecream -----------------------
ic.configureOutput(prefix=f'IC Debug | ', includeContext=True) # DEBUG:
#------------------------------------------------

import time
import sys
#------------------------------------------------
def progress_bar():
    total = 100  
    for i in range(total + 1):
        bar = "#" * (i // 2) + "-" * (50 - i // 2)
        sys.stdout.write(f"\r[{bar}] {i}%")
        sys.stdout.flush()
        time.sleep(0.1)  
    print("\nCompleted!")
#------------------------------------------------

def main():
    
    ic("Hello")
    
    logger.info('-----------------------------------------------------------')
    logger.info('------- Lancement du programme ----------------------------')

    print(is_rclone_installed())                # DEBUG:

    if  is_rclone_installed()  is False: # Check if rclone is installed
        ic("Rclone is not installed")   # DEBUG: 
        logger.error('Rclone is not installed')   # LOG:
    else:
        ic("Rclone is installed")   # DEBUG:
        logger.info(f'Rclone is installed, version: {rclone.version()}')   # LOG:
        ic(rclone.version())  # Get the version of rclone # DEBUG:
        ic(rclone.get_remotes())  # Get a list of available remotes # DEBUG:
        
    while True: # Main menu - Permet de boucler dans l'application
        answer = inquirer.select("Choisir une action",      # Menu principal
        choices=["Remotes existants",
                "Nouveau Remote",
                "Start Progress Bar",
                Choice(value="Exit", name="Exit"),
                ] 
                ,default="Exit", # Entrée sélectionnée par défaut
        ).execute()

        logger.info(f"Choix dans le menu:  {answer} ")  # Logue la réponse sélectionnée  LOG:

        if answer == "Remotes existants": # Affiche les remotes existants
            ic(rclone.get_remotes())  # DEBUG:
            logger.info(f"Remotes existants:  {rclone.get_remotes()} ")  # Logue la réponse sélectionnée  LOG:
            remotes_tab = rclone.get_remotes() # Stocke les remotes existants dans un tableau
            print(remotes_tab) # Affiche les remotes existants  DEBUG:



        if answer == "Start Progress Bar":
            progress_bar()

        elif answer == "Exit": # Quitter l'application
            print("Goodbye!")
            break

    """ fav_lang = inquirer.select(
        message = "Choisir une action:",
        choices = ["Remotes existants","Nouveau Remote",  "Kotlin", "Python", "Rust", "Java", "JavaScript"],
        style={"questionmark": "#ff9d00 bold"},
        vi_mode=True,
        style_override=False,
    ).execute()  # Prompt the user to select a favorite language """

    print(f"La réponse est {answer}")  # Print the selected language   

def is_rclone_installed(): # Check if rclone is installed
    try:
        subprocess.check_output(["rclone", "--version"])
        return True
    except FileNotFoundError:
        return False

    

    
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------

if __name__ == "__main__":
        main()