## Exemple de Stackoverflow:  https://stackoverflow.com/questions/75220524/python-cli-menu-with-arrow-keys-on-windows

from InquirerPy import inquirer  # Import the inquirer module

fav_lang = inquirer.select(
    message = "What's your favorite language:",
    choices = ["Go", "Kotlin", "Python", "Rust", "Java", "JavaScript"]
).execute()  # Prompt the user to select a favorite language

print(f"Your favorite language is {fav_lang}")  # Print the selected language   
