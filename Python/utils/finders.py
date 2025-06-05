from utils.colors import YELLOW, GREEN, RED, MAGENTA, CYAN, B_GRAY, RESET

def ask_users_location() -> str:
    users_location = input(f"Please, tell us your {YELLOW}neighborhood{RESET} name: {GREEN}").strip()
    print(f"{RESET}")
    return users_location

def neighborhood_finder(neighbor: str, data: dict):
    if neighbor.isalpha():
        neighbor = neighbor.strip()
    else:
        print(f"{RED}Invalid neighborhood name. DO NOT use special characters.{RESET}")
        return []
    neighbor = neighbor.upper()
    for key in data.keys():
        if neighbor in data[key]:
            print(f"{GREEN}>>>>>>>>>>>>> Neighborhood '{neighbor}' from {key} district found in the database.{RESET}")
            return neighbor            
    else:
        print(f"{RED}Neighborhood '{neighbor}' not found in the database.{RESET}")
        return []

def district_finder(district: str, data: dict):
    if district.isalpha():
        district = district.strip()
    else:
        print(f"{RED}Invalid district name. DO NOT use special characters.{RESET}")
        return []
    district = district.upper()
    if data.get(district):
        print(f"{GREEN}>>>>>>>>>>>>> District '{district}' found in the database.{RESET}")
        return data[district]
    else:
        print(f"{RED}District '{district}' not found in the database.{RESET}")
        return []
