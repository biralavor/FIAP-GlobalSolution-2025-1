from utils.colors import YELLOW, GREEN, RED, MAGENTA, CYAN, B_GRAY, RESET
from utils.validations import does_str_has_space

def ask_users_location(user_type) -> str:
    print(f"Please {GREEN}{user_type}{RESET}, ", end="")
    users_location = input(f"tell us your {YELLOW}neighborhood{RESET} name: {GREEN}").strip()
    print(f"{RESET}")
    return users_location

def neighborhood_finder(user_input: str, data: dict) -> str:
    if does_str_has_space(user_input):
        parsed_user_input = []
        splited_user_input = user_input.strip().split()
        print(splited_user_input)
        for word in splited_user_input:
            if not word.isalpha():
                print(f"{RED}Invalid neighborhood name. DO NOT use special characters.{RESET}")
                return ""
            word = word.upper()
            parsed_user_input.append(word)
        str_user_input = " ".join(parsed_user_input)
    else:
        str_user_input = user_input.upper()
    for key in data.keys():
        if str_user_input in data[key]:
            print(f"{B_GRAY}Neighborhood '{str_user_input}' from {key} district found in the database.{RESET}")
            return str_user_input
    else:
        print(f"{RED}Neighborhood '{user_input}' not found in the database.{RESET}")
        return ""

def district_finder(district: str, data: dict):
    if district.isalpha():
        district = district.strip()
    else:
        print(f"{RED}Invalid district name. DO NOT use special characters.{RESET}")
        return []
    district = district.upper()
    if data.get(district):
        print(f"{B_GRAY}District '{district}' found in the database.{RESET}")
        return data[district]
    else:
        print(f"{RED}District '{district}' not found in the database.{RESET}")
        return []

def neighbor_risk_finder(user_location: str, data_with_rainfall: dict) -> int:
    for district, neighbors in data_with_rainfall.items():
        if user_location in neighbors:
            neighbor_idx = neighbors.index(user_location)
            risk_value = neighbors[neighbor_idx + 1]
            print(f"{B_GRAY}Rainfall risk for {user_location}: {risk_value}{RESET}")
            return risk_value
    return -1