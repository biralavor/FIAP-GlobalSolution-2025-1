import asyncio

from managers.main_menu_manager import data_init_manager
from managers.main_menu_manager import citizen_submenu_manager
from managers.main_menu_manager import agent_submenu_manager
from utils.printers import sirena_title_printer
from utils.printers import main_menu_printer
from utils.printers import invalid_choice
from utils.printers import exiting_printer
from utils.loaders import neighborhood_list_loader
from utils.validations import ask_valid_nbr
from generators.simulators import extreme_rainfall_risk_simulator
from generators.simulators import incident_simulator

async def main():
    parsed_data = data_init_manager()
    neighborhood_list = neighborhood_list_loader(parsed_data)
    sirena_title_printer()
    data_with_rainfall = await extreme_rainfall_risk_simulator(parsed_data)
    if neighborhood_list and data_with_rainfall:
        while True:
            data_with_incidents = incident_simulator(neighborhood_list, data_with_rainfall)
            main_menu_printer()
            choice = ask_valid_nbr()
            match choice:
                case 1:
                    data_with_incidents = citizen_submenu_manager(data_with_rainfall, data_with_incidents)
                case 2:
                    agent_submenu_manager(data_with_rainfall, data_with_incidents)
                case 3:
                    exiting_printer()
                case _:
                    invalid_choice()

if __name__ == '__main__':
    asyncio.run(main())