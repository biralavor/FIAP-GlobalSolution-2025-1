from utils.colors import YELLOW, GREEN, RED, MAGENTA, CYAN, B_GRAY, RESET

def ask_valid_nbr() -> int:
    while True:
        user_input = input(f"{CYAN}Please choose an option: {GREEN}").strip()
        try:
            user_input = int(user_input)
            if user_input > 0:
                break
        except ValueError:
            print(f"{RED}Invalid input. Please enter a positive integer.{RESET}")
    print(f"{RESET}")
    return user_input