from InquirerPy import inquirer
import time
import sys

def progress_bar():
    total = 100  
    for i in range(total + 1):
        bar = "#" * (i // 2) + "-" * (50 - i // 2)
        sys.stdout.write(f"\r[{bar}] {i}%")
        sys.stdout.flush()
        time.sleep(0.1)  
    print("\nCompleted!")


def main_menu():
    while True:
        answer = inquirer.select(
            "What would you like to do?",
            choices=["Start Progress Bar", "Exit"]
        ).execute()

        if answer == "Start Progress Bar":
            progress_bar()
        elif answer == "Exit":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main_menu()