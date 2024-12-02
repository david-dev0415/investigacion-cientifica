from colorama import Fore, Style


def successMessage(message):
    print(Fore.GREEN + "✅ " + message)


def errorMessage(message):
    print(Fore.RED + "❌ " + message)


def warningMessage(message):
    print(Fore.YELLOW + "⚠️ " + message)
