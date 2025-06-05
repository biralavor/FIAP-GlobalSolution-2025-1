import asyncio

from utils.printers import main_menu_printer
from utils.printers import citizen_menu_printer
from utils.printers import invalid_choice
from utils.printers import neighborhood_printer
from utils.validations import ask_valid_nbr
from utils.finders import neighborhood_finder
from utils.finders import ask_users_location
from utils.loaders import csv_loader
from utils.loaders import csv_parser
from utils.simulations import rainfall_simulation

SP_NEIGHBORHOODS = "database-files/distritos-sp.csv"


async def main():
    data = csv_loader(SP_NEIGHBORHOODS)
    parsed_data = csv_parser(data)
    neighborhood_printer(parsed_data)
    await rainfall_simulation()
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
                        case 2:
                            print("Checking if you are in danger...")
                        case 3:
                            break
            case 2:
                print("Loading City Patrol Agent System...")
                agent_location = ask_users_location()
                neighborhood_finder(agent_location, parsed_data)
            case 3:
                print("Exiting S.I.R.E.N.A. System. Goodbye!")
                exit(0)
            case _:
                invalid_choice()
                citizen_menu_printer()

if __name__ == '__main__':
    asyncio.run(main())