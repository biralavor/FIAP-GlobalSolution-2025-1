import asyncio

from managers.main_menu_manager import citizen_manager
from managers.main_menu_manager import agent_manager
from utils.printers import sirena_title_printer
from utils.printers import main_menu_printer
from utils.printers import invalid_choice
from utils.printers import exiting_printer
from utils.printers import clear_screen
from utils.loaders import csv_loader
from utils.loaders import csv_parser
from utils.loaders import neighborhood_list_loader
from utils.validations import ask_valid_nbr
from generators.simulators import rainfall_init
from generators.simulators import extreme_rainfall_risk_simulator
from generators.simulators import incident_simulator

SP_NEIGHBORHOODS = "database-files/distritos-sp.csv"

async def main():
    data = csv_loader(SP_NEIGHBORHOODS)
    parsed_data = csv_parser(data)
    neighborhood_list = neighborhood_list_loader(parsed_data)
    data_with_rainfall = rainfall_init(parsed_data)
    data_with_rainfall = await extreme_rainfall_risk_simulator(data_with_rainfall)
    neighborhood_list = await incident_simulator(neighborhood_list, data_with_rainfall)
    clear_screen()
    sirena_title_printer()
    while True:
        main_menu_printer()
        choice = ask_valid_nbr()
        match choice:
            case 1:
                if neighborhood_list:
                    neighborhood_list = citizen_manager(data_with_rainfall, neighborhood_list)
            case 2:
                agent_manager(data_with_rainfall, neighborhood_list)
            case 3:
                exiting_printer()
            case _:
                invalid_choice()

if __name__ == '__main__':
    asyncio.run(main())