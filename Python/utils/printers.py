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
    print(f"{MAGENTA}Exiting S.I.R.E.N.A. >>> Goodbye and {GREEN}be safe!{RESET}")
    exit(0)

def sirena_title_printer():
    print(f"Welcome to {MAGENTA}S.I.R.E.N.A.{RESET}")
    print(f"{CYAN}")
    print("            (_)")
    print("       ___   _   _ __ ___   _ __    __ _ ")
    print("      / __| | | | '__/ _ \\ | '_ \\  / _` | ")
    print("      \\__ \\_| |_| |_|  __/_| | | || (_| |")
    print("      |___(_)_(_)_(_)\\___(_)_| |_(_)__,_(_)\n")
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

def citizen_menu_printer(citizen_loop):
    if citizen_loop:
        print(f"Welcome {GREEN}CITIZEN{RESET}!")
    else:
        print(f"{MAGENTA}Choose your next move, {GREEN}CITIZEN!{RESET}")
    print(f"{YELLOW}1.{RESET} Report Incident")
    print(f"{YELLOW}2.{RESET} Am I in Danger ???")
    print(f"{YELLOW}3.{RESET} Back to Main Menu")

def agent_menu_printer(agent_loop):
    if agent_loop:
        print(f"Welcome {GREEN}AGENT{RESET}!")
    else:
        print(f"{MAGENTA}Choose your next move, {GREEN}AGENT!{RESET}")
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

def incidents_table_printer(incident_dict: dict) -> None:
    print(f"{YELLOW}-{RESET}" * 55)
    print(f"| {MAGENTA}CONFIDENCE{RESET}    |   {MAGENTA}INCIDENTS{RESET}\t| {MAGENTA}  LOCATION{RESET}\t|")
    print(f"{YELLOW}-{RESET}" * 55)
    for location, values in incident_dict.items():
        incidents_value = values[0]
        confidence = values[1]
        if confidence == "High":
            confidence = f"{RED}{confidence}{RESET}"
            location = f"{RED}{location}{RESET}"
        elif confidence == "Med":
            confidence = f"{YELLOW}{confidence}{RESET}"
            location = f"{YELLOW}{location}{RESET}"
        print(f"|   {confidence} \t| \t{incidents_value} \t| {location}\t|")
        print(f"{B_GRAY}-{RESET}" * 50)

def high_risk_district_printer(agent_location: str, data_with_rainfall: dict, neighborhood_list: dict) -> None:
    print(f"{YELLOW}-{RESET}" * 55)
    print(f"| {MAGENTA}CONFIDENCE{RESET}    |   {MAGENTA}INCIDENTS{RESET}\t| {MAGENTA}  LOCATION{RESET}\t|")
    print(f"{YELLOW}-{RESET}" * 55)
    for district, all_neighbors in data_with_rainfall.items():
        for neighbor in all_neighbors:
            if agent_location == neighbor:
                district_list = data_with_rainfall[district]
                for each_neighbor in district_list:
                    if each_neighbor in neighborhood_list:
                        incidents_value = neighborhood_list[each_neighbor][0]
                        confidence = neighborhood_list[each_neighbor][1]
                        if confidence == "High":
                            confidence = f"{RED}{confidence}{RESET}"
                            each_neighbor = f"{RED}{each_neighbor}{RESET}"
                            print(f"|   {confidence} \t| \t{incidents_value} \t| {each_neighbor}\t|")
                            print(f"{B_GRAY}-{RESET}" * 50)

def citizen_danger_printer(user_location: str, neighborhood_list: dict):
    for neighborhood, values in neighborhood_list.items():
        if user_location == neighborhood:
            reported_incidents = values[0]
            confidence = values[1]
            print(f"You're in a high-risk area: {neighborhood}")
            print(f"Number of incidents there is: {reported_incidents}")
            print(f"Confidence index: {confidence}")

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

