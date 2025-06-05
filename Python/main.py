from utils.colors import YELLOW, GREEN, RED, MAGENTA, CYAN, B_GRAY, RESET
from utils.printers import main_menu_printer
from utils.printers import citizen_menu_printer
from utils.printers import invalid_choice
from utils.printers import neighborhood_printer
from utils.validations import ask_valid_nbr
from utils.finders import neighborhood_finder
from utils.finders import ask_users_location
from utils.loaders import csv_loader
from utils.loaders import csv_parser

SP_NEIGHBORHOODS = "database-files/distritos-sp.csv"


def main():
    data = csv_loader(SP_NEIGHBORHOODS)
    parsed_data = csv_parser(data)
    neighborhood_printer(parsed_data)
    while True:
        main_menu_printer()
        choice = ask_valid_nbr()
        match choice:
            case 1:
                citizen_location = ask_users_location()
                neighborhood_finder(citizen_location, parsed_data)
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
                agent_location = ask_users_location()
                neighborhood_finder(agent_location, parsed_data)
                # Here you would call the function for city patrol agent options
            case 3:
                print("Exiting S.I.R.E.N.A. System. Goodbye!")
                return
            case _:
                invalid_choice()
                citizen_menu_printer()

if __name__ == '__main__':
    main()