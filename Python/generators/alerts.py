from utils.colors import YELLOW, GREEN, RED, MAGENTA, CYAN, B_GRAY, RESET

def alert_generator(risk_value):
    if risk_value == 0:
        print(f"\nNo risk detected. Enjoy your day!")
    elif risk_value == 1:
        print(f"\nLow risk detected. Stay alert!")
    elif risk_value == 2:
        print(f"\nModerate risk detected. Take precautions!")
    elif risk_value == 3:
        print(f"\nHigh risk detected. Evacuate if necessary!")
    elif risk_value == 4:
        print(f"\nEXTREME risk detected!")
        print(f"{MAGENTA}Go to the higher altitude at 'B' location!{RESET}")
        evacuation_plan_printer()
    else:
        print(f"Invalid risk value.")


def evacuation_plan_printer():
    print(f"{RED}")
    print(" _      ______     __      ________   _   _  ______          __")
    print("| |    |  ____|   /\\ \\    / /  ____| | \\ | |/ __ \\ \\        / /")
    print("| |    | |__     /  \\ \\  / /| |__    |  \\| | |  | \\ \\  /\\  / / ")
    print("| |    |  __|   / /\\ \\ \\/ / |  __|   | . ` | |  | |\\ \\/  \\/ /  ")
    print("| |____| |____ / ____ \\  /  | |____  | |\\  | |__| | \\  /\\  /   ")
    print("|______|______/_/    \\_\\/   |______| |_| \\_|\\____/   \\/  \\/    ")
    print("---------------------------------------------------------------------")
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