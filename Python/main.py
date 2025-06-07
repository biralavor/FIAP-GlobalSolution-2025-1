import asyncio

from utils.printers import sirena_title_printer
from utils.printers import main_menu_printer
from utils.printers import citizen_menu_printer
from utils.printers import agent_menu_printer
from utils.printers import invalid_choice
from utils.printers import exiting_printer
from utils.printers import clear_screen
from utils.validations import ask_valid_nbr
from utils.loaders import csv_loader
from utils.loaders import csv_parser
from utils.loaders import neighborhood_list_loader
from managers.neighbor_manager import neighborhood_manager
from generators.simulators import rainfall_init
from generators.simulators import extreme_rainfall_risk_simulator
from generators.simulators import incident_simulator
from managers.incident_manager import incident_manager

SP_NEIGHBORHOODS = "database-files/distritos-sp.csv"


async def main():
    data = csv_loader(SP_NEIGHBORHOODS)
    parsed_data = csv_parser(data)
    neighborhood_list = neighborhood_list_loader(parsed_data)
    data_with_rainfall = rainfall_init(parsed_data)
    data_with_rainfall = await extreme_rainfall_risk_simulator(data_with_rainfall)
    neighborhood_list = await incident_simulator(neighborhood_list)
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
                    while True:
                        citizen_menu_printer()
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
            case 2:
                user_type = "AGENT"
                agent_menu_printer()
                incident_manager(neighborhood_list)
                exit(0)
            case 3:
                exiting_printer()
            case _:
                invalid_choice()
                citizen_menu_printer()
        clear_screen()

if __name__ == '__main__':
    asyncio.run(main())