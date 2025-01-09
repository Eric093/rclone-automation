## Exemple de Stackoverflow:  https://stackoverflow.com/questions/75220524/python-cli-menu-with-arrow-keys-on-windows
# Avec ajout RCLONE


from InquirerPy import inquirer  # Import the inquirer module
#from rclone_python import rclone  # Import the rclone module  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import logging  ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#logging.basicConfig(filename="fichier.log", level=logging.DEBUG)

## Paramétrage des logs -------------------------
from logging.handlers import RotatingFileHandler
logging.basicConfig(filename='log/programlog.log', level=logging.DEBUG, encoding='utf-8', format=' %(asctime)s - %(levelname)s -  %(message)s')

from rclone_python import rclone  # Import the rclone module

logger = logging.getLogger(__name__)
# ----------------------------------------------

from icecream import ic # Outil de debug
## Paramétrage d'icecream -----------------------
ic.configureOutput(prefix=f'IC Debug | ', includeContext=True)
#------------------------------------------------


def main():
    #logging.basicConfig(filename='log/programlog.txt', level=logging.DEBUG, encoding='utf-8', format=' %(asctime)s - %(levelname)s -  %(message)s')
    #logging.debug("-- Démarrage traitement")
    ic("Hello")
    
    logger.debug('-----------------------------------------------------------')
    logger.debug('------- Lancement du programme ----------------------------')
    
    if  is_rclone_installed()  is False: # Check if rclone is installed
        print("Rclone n'est pas installé !")

    fav_lang = inquirer.select(
        message = "What's your favorite language:",
        choices = ["Prout", "Kotlin", "Python", "Rust", "Java", "JavaScript"]
    ).execute()  # Prompt the user to select a favorite language

    print(f"Your favorite language is {fav_lang}")  # Print the selected language   

def is_rclone_installed(): # Check if rclone is installed
    if rclone.is_installed():
        print("Rclone is installed")
        return True
    else:
        #print("Rclone n'est pas installé !")
        return False

if __name__ == "__main__":
    #logger = logging.getLogger(__name__)
    #logger.debug('---- Démarrage programme ----------------------------')
    main()