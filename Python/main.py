import asyncio

from utils.printers import sirena_title_printer
from utils.printers import main_menu_printer
from utils.printers import citizen_menu_printer
from utils.printers import invalid_choice
from utils.printers import exiting_printer
from utils.printers import clear_screen
from utils.validations import ask_valid_nbr
from utils.loaders import csv_loader
from utils.loaders import csv_parser
from managers.neighbor_manager import neighborhood_manager
from generators.simulators import rainfall_init
from generators.simulators import extreme_rainfall_risk_simulator


SP_NEIGHBORHOODS = "database-files/distritos-sp.csv"


async def main():
    data = csv_loader(SP_NEIGHBORHOODS)
    parsed_data = csv_parser(data)
    data_with_rainfall = rainfall_init(parsed_data)
    data_with_rainfall = await extreme_rainfall_risk_simulator(data_with_rainfall)
    clear_screen()
    sirena_title_printer()
    while True:
        main_menu_printer()
        choice = ask_valid_nbr()
        match choice:
            case 1:
                user_type = "CITIZEN"
                risk_value = neighborhood_manager(user_type, data_with_rainfall)
                if risk_value < 4:
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
                            case _:
                                invalid_choice()
                                citizen_menu_printer()
            case 2:
                user_type = "AGENT"
                # neighborhood_manager(user_type, data_with_rainfall)
            case 3:
                exiting_printer()
            case _:
                invalid_choice()
                citizen_menu_printer()
        clear_screen()

if __name__ == '__main__':
    asyncio.run(main())