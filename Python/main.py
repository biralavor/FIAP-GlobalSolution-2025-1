from utils.colors import YELLOW, GREEN, RED, MAGENTA, CYAN, B_GRAY, RESET
from utils.printers import main_menu_printer
from utils.printers import citizen_menu_printer
from utils.printers import invalid_choice
from utils.validations import ask_valid_nbr

def main():
    while True:
        main_menu_printer()
        choice = ask_valid_nbr()
        match choice:
            case 1:
                citizen_menu_printer()
                while True:
                    citizen_choice = ask_valid_nbr()
                    match citizen_choice:
                        case 1:
                            print("Reporting Incident...")
                            # Here you would call the function to report an incident
                        case 2:
                            print("Checking if you are in danger...")
                            # Here you would call the function to check danger status
                        case 3:
                            break
            case 2:
                print("Loading City Patrol Agent System...")
                # Here you would call the function for city patrol agent options
            case 3:
                print("Exiting S.I.R.E.N.A. System. Goodbye!")
                return
            case _:
                invalid_choice()
                citizen_menu_printer()

if __name__ == '__main__':
    main()