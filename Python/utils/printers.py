from utils.colors import YELLOW, GREEN, RED, MAGENTA, CYAN, B_GRAY, RESET

def main_menu_printer():
    print(f"Welcome to {MAGENTA}S.I.R.E.N.A.{RESET}")
    print(f"{MAGENTA}S{RESET}istema {MAGENTA}I{RESET}ntegrado de ", end="")
    print(f"{MAGENTA}RE{RESET}sposta à {MAGENTA}E{RESET}mergências e ", end="")
    print(f"{MAGENTA}N{RESET}otificações {MAGENTA}A{RESET}mbientais")
    print(f"{GREEN}---------------------------------{RESET}")
    print(f"{YELLOW}1.{RESET} Are you a Citizen ?")
    print(f"{YELLOW}2.{RESET} Are you a City Patrol Agent ?")
    print(f"{YELLOW}3.{RESET} Exit")

def citizen_menu_printer():
    print("Loading S.I.R.E.N.A. Alerts System...")
    print("Welcome CITIZEN!")
    print(f"{YELLOW}1.{RESET} Report Incident")
    print(f"{YELLOW}2.{RESET} Am I in Danger ???")
    print(f"{YELLOW}3.{RESET} Back to Main Menu")

def invalid_choice():
    print(f"{RED}Invalid choice. Please try again.{RESET}")

#*********************************************************************

