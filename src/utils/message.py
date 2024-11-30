from colorama import Fore, Style

def successMessage(message):
    print("\n" + Fore.GREEN + "✅ " + message)

def errorMessage(message):
    print("\n" + Fore.RED + "❌ " + message)

def warningMessage(message):
    print("\n" + Fore.YELLOW + "⚠️ " + message)

