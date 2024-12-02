# import menu
from src import menu
from colorama import Fore, Back, Style, init

init(autoreset=True)

if __name__ == "__main__":
    print(
        Style.BRIGHT
        + Fore.WHITE
        + "\n-----------------------------------------------------------------------"
    )
    print(
        Style.BRIGHT
        + Fore.MAGENTA
        + "🔬 Bienvenido al sistema de gestión de datos de experimentos. 🧠 "
    )
    print(
        Style.BRIGHT
        + Fore.WHITE
        + "-----------------------------------------------------------------------"
    )
    menu.run()

    # Inicializar colorama

    # Impresiones con colores y estilos
    # print(Fore.RED + "Este texto es rojo.")
    # print(Fore.GREEN + "Este texto es verde.")
    # print(Back.YELLOW + "Este texto tiene un fondo amarillo.")
    # print(Style.BRIGHT + "Este texto es brillante.")
    # print(Fore.BLUE + Back.WHITE + "Texto azul con fondo blanco")
    # print(Style.DIM + Fore.MAGENTA + "Texto magenta tenue")

    # init(autoreset=True)
