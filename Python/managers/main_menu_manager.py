from managers.incident_manager import incident_manager
from managers.neighbor_manager import neighborhood_manager
from utils.printers import citizen_menu_printer
from utils.printers import citizen_danger_printer
from utils.printers import agent_menu_printer
from utils.printers import high_risk_district_printer
from utils.printers import invalid_choice
from utils.finders import ask_users_location
from utils.validations import is_agent_in_high_risk_district
from utils.validations import ask_valid_nbr
from utils.colors import YELLOW, GREEN, RED, MAGENTA, CYAN, B_GRAY, RESET

def citizen_manager(data_with_rainfall: dict, neighborhood_list: dict):
    user_type = "CITIZEN"
    user_location = ask_users_location(user_type)
    risk_value = neighborhood_manager(user_type, user_location, data_with_rainfall)
    if risk_value < 4:
        while True:
            citizen_first_loop = True
            citizen_menu_printer(citizen_first_loop)
            citizen_first_loop = False
            citizen_choice = ask_valid_nbr()
            match citizen_choice:
                case 1:
                    print("Reporting Incident...")
                case 2:
                    citizen_danger_printer(user_location, neighborhood_list)
                case 3:
                    break
                case _:
                    invalid_choice()

def agent_manager(data_with_rainfall, neighborhood_list):
    user_type = "AGENT"
    agent_first_loop = True
    while True:
        agent_menu_printer(agent_first_loop)
        agent_first_loop = False
        agent_choice = ask_valid_nbr()
        match agent_choice:
            case 1:
                agent_location = ask_users_location(user_type)
                print(f"{MAGENTA}Taking you to the nearest incident from {YELLOW}{agent_location}...{RESET}")
                is_agent_in_high_risk_district(agent_location, data_with_rainfall, neighborhood_list)
                high_risk_district_printer(agent_location, data_with_rainfall, neighborhood_list)
            case 2:
                incident_manager(neighborhood_list)
            case 3:
                break
            case _:
                invalid_choice()
