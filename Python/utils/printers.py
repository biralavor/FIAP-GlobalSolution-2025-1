import os

from utils.colors import YELLOW, GREEN, RED, MAGENTA, CYAN, B_GRAY, RESET

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    elif os.name == 'mac':
        os.system('clear')

def invalid_choice():
    print(f"{RED}Invalid choice. Please try again.{RESET}")

def exiting_printer():
    print(f"{MAGENTA}>>> Exiting S.I.R.E.N.A. Goodbye and {GREEN}be safe!{RESET}")
    exit(0)

def sirena_title_printer():
    print(f"Welcome to {MAGENTA}S.I.R.E.N.A.{RESET}")
    print(f"{CYAN}")
    print("            (_)")
    print("       ___   _   _ __ ___   _ __    __ _ ")
    print("      / __| | | | '__/ _ \\ | '_ \\  / _` | ")
    print("      \\__ \\_| |_| |_|  __/_| | | || (_| |")
    print("      |___(_)_(_)_(_)\\___(_)_| |_(_)__,_(_)")
    print(f"{GREEN}---------------------------------{RESET}")
    print(f"| {MAGENTA}S{RESET}istema {MAGENTA}I{RESET}ntegrado de ", end="")
    print(f"{MAGENTA}R{RESET}sposta às {MAGENTA}E{RESET}mergências e ", end="")
    print(f"{MAGENTA}N{RESET}otificações {MAGENTA}A{RESET}mbientais |")
    print(f"{GREEN}---------------------------------{RESET}")
    print(f"{RESET}")

def main_menu_printer():
    print(f"{MAGENTA}Tell us who are you:{RESET}")
    print(f"{YELLOW}1.{RESET} Citizen")
    print(f"{YELLOW}2.{RESET} City Patrol Agent")
    print(f"{YELLOW}3.{RESET} Exit")

def citizen_menu_printer():
    print(f"Welcome {GREEN}CITIZEN{RESET}!")
    print(f"{YELLOW}1.{RESET} Report Incident")
    print(f"{YELLOW}2.{RESET} Am I in Danger ???")
    print(f"{YELLOW}3.{RESET} Back to Main Menu")

def agent_menu_printer():
    print(f"Welcome {GREEN}AGENT{RESET}!")
    print(f"{YELLOW}1.{RESET} Take me to the nearest incident")
    print(f"{YELLOW}2.{RESET} Show ALL Incident's List")
    print(f"{YELLOW}3.{RESET} Back to Main Menu")

def neighborhood_printer(neighborhoods: dict):
    if neighborhoods:
        print(f"{B_GRAY}Neighborhoods in the database:{RESET}")
        for index, (key, value) in enumerate(neighborhoods.items(), start=1):
            print(f"{YELLOW}{index}.{RESET} {key}: {value}")
    else:
        print(f"{RED}No neighborhoods found.{RESET}")

def leave_now_printer():
    print(f"{RED}")
    print(" _      ______     __      ________   _   _  ______          __  _ ")
    print("| |    |  ____|   /\\ \\    / /  ____| | \\ | |/ __ \\ \\        / / | |")
    print("| |    | |__     /  \\ \\  / /| |__    |  \\| | |  | \\ \\  /\\  / /  | |")
    print("| |    |  __|   / /\\ \\ \\/ / |  __|   | . ` | |  | |\\ \\/  \\/ /   | |")
    print("| |____| |____ / ____ \\  /  | |____  | |\\  | |__| | \\  /\\  /    |_|")
    print("|______|______/_/    \\_\\/   |______| |_| \\_|\\____/   \\/  \\/     (_)")
    print(f"{RESET}")

def evacuation_plan_printer():
    print(f"{YELLOW}")
    print("                                                   .@@%#%#+.")
    print("                                                   .@@   #@-")
    print("                                                   .@@###@+")
    print("                                                   .@@..:#@=")
    print("                                         ::-==::   .@@--=%@=")
    print("                              =*###@@@@@@@@@@@@@    =====-.")
    print("                              -+++++%@@@@@@@@@@*")
    print("                                    +@@@@@@@@@*")
    print("                               .-=#@@@@@@@@@@*")
    print("                            -=%@@@@@@*-#@@@@=")
    print("         .%@@-           :=#%@@@@@#-.    @@@@")
    print("         *@-%%.      .:=#@@@@%*=.       *@@%:")
    print("        -@* -@*      =@@@@%-.           *#=.")
    print("       .%@###@@-      .===")
    print("       *@=...:@%.")
    print("      .==     -=-")
    print(f"{RESET}")

#*********************************************************************

