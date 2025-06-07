from utils.finders import ask_users_location
from utils.finders import neighbor_risk_finder
from utils.finders import neighborhood_finder
from utils.validations import does_str_has_special_char
from generators.alerts import alert_generator
from utils.colors import YELLOW, GREEN, RED, MAGENTA, CYAN, B_GRAY, RESET


def neighborhood_manager(user_type: str, data_with_rainfall: dict) -> int:
    user_location = ask_users_location(user_type)
    while does_str_has_special_char(user_location) or user_location.isnumeric():
        if user_location.isnumeric():
            print(f"{RED}Numbers are NOT allowed for locations.{RESET}")
        user_location = ask_users_location(user_type)
    neighbor = neighborhood_finder(user_location, data_with_rainfall)
    if neighbor:
        risk_value = neighbor_risk_finder(neighbor, data_with_rainfall)
        alert_generator(risk_value)
        if risk_value == 4:
            exit(0)
    else:
        risk_value = neighborhood_manager(user_type, data_with_rainfall)
    return risk_value