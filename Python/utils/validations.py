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

def does_str_has_space(user_input: str) -> bool:
    for single_char in user_input:
        if single_char == " ":
            return True
    return False

def does_str_has_special_char(user_input: str) -> bool:
    found = False
    special_chars_bunk = "áàâãéèêíïóôõöúçÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇ!@#$%^&*()_+-={}[]|\\:;\"'<>,.?/~`ñýźżźŕŕřšşśťţþďđğģħĵķłľĺńňņŋñṕŕřśşšťţṿẃẍýźżž"
    if does_str_has_space(user_input):
        splited_input = user_input.strip().split()
        for word in splited_input:
            for special_char in special_chars_bunk:
                if special_char in word:
                    found = True
    else:
        for special_char in special_chars_bunk:
            if special_char in user_input:
                found = True
    if found:
        print(f"{RED}Invalid neighborhood name. DO NOT use special characters.{RESET}")
        return True
    else:
        return False

def is_agent_in_high_risk_district(agent_location: str, data_with_rainfall: dict, neighborhood_list: dict) -> bool:
    its_a_match = False
    for district, neighborhood in data_with_rainfall.items():
        if agent_location in neighborhood:
            for neighborhood, values_list in neighborhood_list.items():
                if values_list[1] == "High":
                    its_a_match = True
                    actual_district = district
                    break
    if its_a_match:
        print(f"{B_GRAY}S.I.R.E.N.A. is thinking ::: Agent is in a high-risk district: {actual_district}{RESET}")
        return True
    else:
        print(f"{B_GRAY}S.I.R.E.N.A. is thinking ::: Agent is NOT in a high-risk district.{RESET}")
        return False
