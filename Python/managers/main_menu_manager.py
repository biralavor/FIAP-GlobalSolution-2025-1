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

def citizen_submenu_manager(data_with_rainfall: dict, neighborhood_list: dict) -> None:
    """
    Brief:
        This function manages the citizen's submenu, allowing them to report incidents
        and view danger levels in their neighborhood.
    Args:
        `data_with_rainfall` (dict): A dictionary containing rainfall data and neighborhood information.
        `neighborhood_list` (dict): A dictionary containing neighborhoods and their incident values.
    Returns:
        `None`
    """
    user_type = "CITIZEN"
    first_time_report = True
    user_location = ask_users_location(user_type)
    risk_value = neighborhood_manager(user_type, user_location, data_with_rainfall)
    citizen_first_loop = True
    if risk_value < 4:
        while True:
            citizen_menu_printer(citizen_first_loop)
            citizen_first_loop = False
            citizen_choice = ask_valid_nbr()
            match citizen_choice:
                case 1:
                    if first_time_report:
                        neighborhood_list = citizen_report_creator(user_location, neighborhood_list)
                        first_time_report = False
                    else:
                        print(f"{RED}You can't add a report for the same location.{RESET}")
                case 2:
                    citizen_danger_printer(user_location, neighborhood_list)
                case 3:
                    break
                case _:
                    invalid_choice()

def agent_submenu_manager(data_with_rainfall: dict, neighborhood_list: dict) -> None:
    """
    Brief:
        This function manages the agent's submenu, allowing them to view incidents
        in high-risk districts and manage incidents.
    Args:
        `data_with_rainfall` (dict): A dictionary containing rainfall data and neighborhood information.
        `neighborhood_list` (dict): A dictionary containing neighborhoods and their incident values.
    Returns:
        `None`
    """
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
                if is_agent_in_high_risk_district(agent_location, data_with_rainfall, neighborhood_list):
                    high_risk_district_printer(agent_location, data_with_rainfall, neighborhood_list)
                else:
                    print(f"{MAGENTA}Agent, you're {YELLOW}NOT{MAGENTA} in a high-risk district.{RESET}")
            case 2:
                incident_manager(neighborhood_list)
            case 3:
                break
            case _:
                invalid_choice()

def citizen_report_creator(user_location: str, neighborhood_list: dict) -> dict:
    if user_location in neighborhood_list:
        incident_value = neighborhood_list[user_location][0]
        print(f"{B_GRAY}S.I.R.E.N.A. is thinking ::: {user_location} is with value {incident_value} reported incidents.{RESET}")
        incident_value += 1
        neighborhood_list[user_location][0] = incident_value
        print(f"{MAGENTA}Reporting incident from {YELLOW}{user_location}{MAGENTA} now!{RESET}")
        print(f"{B_GRAY}S.I.R.E.N.A. is thinking ::: {user_location} is with value {incident_value} reported incidents.{RESET}")
    return neighborhood_list