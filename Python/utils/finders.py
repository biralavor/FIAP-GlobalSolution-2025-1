from utils.colors import YELLOW, GREEN, RED, MAGENTA, CYAN, B_GRAY, RESET
from utils.validations import does_str_has_space
from utils.validations import does_str_has_special_char

def ask_users_location(user_type) -> str:
    print(f"Please {GREEN}{user_type}{RESET}, ", end="")
    users_location = input(f"tell us your {YELLOW}neighborhood{RESET} name: {B_GRAY}('cancel' to exit) {GREEN}").strip()
    print(f"{RESET}")
    while does_str_has_special_char(users_location) or users_location.isnumeric():
        if users_location.isnumeric():
            print(f"{RED}Numbers are NOT allowed for locations.{RESET}")
        users_location = ask_users_location(user_type)
    return users_location.upper()

def user_input_str_parser(user_input: str) -> str:
    if does_str_has_space(user_input):
        parsed_user_input = []
        splited_user_input = user_input.strip().split()
        for word in splited_user_input:
            word = word.upper()
            parsed_user_input.append(word)
        str_user_input = " ".join(parsed_user_input)
    else:
        str_user_input = user_input.upper()
    return str_user_input

def neighborhood_finder(user_input: str, data: dict) -> str:
    if user_input == "CANCEL":
        print(f"{YELLOW}Operation cancelled.{RESET}")
        exit(0)
    parsed_input = user_input_str_parser(user_input)
    for key in data.keys():
        if parsed_input in data[key]:
            print(f"{B_GRAY}S.I.R.E.N.A. is thinking ::: Neighborhood '{parsed_input}' from {key} district found in the database.{RESET}")
            return parsed_input
    else:
        print(f"{RED}Neighborhood '{user_input}' not found in the database.{RESET}")
        return ""

def district_finder(user_input: str, data: dict):
    parsed_input = user_input_str_parser(user_input)
    if data.get(parsed_input):
        print(f"{B_GRAY}S.I.R.E.N.A. is thinking ::: District '{parsed_input}' found in the database.{RESET}")
        return data[parsed_input]
    else:
        print(f"{RED}District '{parsed_input}' not found in the database.{RESET}")
        return []

def neighbor_risk_finder(user_location: str, data_with_rainfall: dict) -> int:
    for district, neighbors in data_with_rainfall.items():
        if user_location in neighbors:
            neighbor_idx = neighbors.index(user_location)
            risk_value = neighbors[neighbor_idx + 1]
            print(f"{B_GRAY}S.I.R.E.N.A. is thinking ::: Rainfall risk for {user_location}: {risk_value}{RESET}")
            return risk_value
    return -1

