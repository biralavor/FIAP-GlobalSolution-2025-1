import asyncio

from utils.printers import main_menu_printer
from utils.printers import citizen_menu_printer
from utils.printers import invalid_choice
from utils.printers import exiting_printer
from utils.validations import ask_valid_nbr
from utils.finders import neighborhood_finder
from utils.finders import ask_users_location
from utils.finders import neighbor_risk_finder
from utils.loaders import csv_loader
from utils.loaders import csv_parser
from generators.simulators import rainfall_init
from generators.simulators import extreme_rainfall_risk_simulator

SP_NEIGHBORHOODS = "database-files/distritos-sp.csv"


async def main():
    data = csv_loader(SP_NEIGHBORHOODS)
    parsed_data = csv_parser(data)
    data_with_rainfall = rainfall_init(parsed_data)
    data_with_rainfall = await extreme_rainfall_risk_simulator(data_with_rainfall)
    while True:
        main_menu_printer()
        choice = ask_valid_nbr()
        match choice:
            case 1:
                while True:
                    user_location = ask_users_location("CITIZEN")
                    neighbor = neighborhood_finder(user_location, data_with_rainfall)
                    if neighbor:
                        risk_value = neighbor_risk_finder(neighbor, data_with_rainfall)
                        break
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
                user_location = ask_users_location("AGENT")
                neighborhood_finder(user_location, data_with_rainfall)
            case 3:
                exiting_printer()
            case _:
                invalid_choice()
                citizen_menu_printer()

if __name__ == '__main__':
    asyncio.run(main())