from utils.colors import YELLOW, GREEN, RED, MAGENTA, CYAN, B_GRAY, RESET
from utils.printers import incidents_table_printer

def incident_manager(neighborhood_list: dict) -> None:
    items_list = list(neighborhood_list.items())
    sorted_items = sorted(items_list, key=get_incident_value, reverse=True)
    print(f"{B_GRAY}S.I.R.E.N.A. is thinking ::: Sorting incidents by risk value...{RESET}")
    sorted_incidents_as_dict = dict(sorted_items)
    incidents_table_printer(sorted_incidents_as_dict)

def get_incident_value(item: tuple) -> int:
    selected_data = item[1][0]
    return selected_data
