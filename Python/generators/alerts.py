from utils.colors import YELLOW, GREEN, RED, MAGENTA, CYAN, B_GRAY, RESET
from utils.printers import evacuation_plan_printer
from utils.printers import leave_now_printer

def alert_generator(risk_value):
    if risk_value == 0:
        print(f"\n{GREEN}No risk detected. Enjoy your day!{RESET}")
    elif risk_value == 1:
        print(f"\n{GREEN}Low risk detected. {MAGENTA}Stay alert!{RESET}")
    elif risk_value == 2:
        print(f"\n{YELLOW}Moderate risk detected. {MAGENTA}Take precautions!{RESET}")
    elif risk_value == 3:
        print(f"\n{RED}High risk detected. {MAGENTA}Evacuate if necessary!{RESET}")
        print(f"{MAGENTA}Here is your {YELLOW}EVACUATION PLAN:{RESET}")
        evacuation_plan_printer()
    elif risk_value == 4:
        print(f"\n{RED}EXTREME risk detected!{RESET}")
        print(f"{YELLOW}GO TO THE HIGHER ALTITUDE AT 'B' LOCATION NOW!{RESET}")
        leave_now_printer()
        evacuation_plan_printer()
    else:
        print(f"Invalid risk value.")

