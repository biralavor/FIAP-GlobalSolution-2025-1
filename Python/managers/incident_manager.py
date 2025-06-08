from utils.colors import YELLOW, GREEN, RED, MAGENTA, CYAN, B_GRAY, RESET
from utils.printers import incidents_table_printer

def incident_manager(neighborhood_list: dict) -> None:
    """
    Brief:
        This function manages the sorting of incidents based on their risk value.
    Args:
        `neighborhood_list` (dict): A dictionary where keys are neighborhoods and values are lists containing
                                     the number of incidents and confidence level. The sort method uses
                                     the number of incidents as the key for sorting, in descending order.
    Returns:
        `None`
    """
    items_list = list(neighborhood_list.items())
    sorted_items = sorted(items_list, key=get_incident_value, reverse=True)
    print(f"{B_GRAY}S.I.R.E.N.A. is thinking ::: Sorting incidents by risk value...{RESET}")
    sorted_incidents_as_dict = dict(sorted_items)
    incidents_table_printer(sorted_incidents_as_dict)

def get_incident_value(item: tuple) -> int:
    """
    Brief:
        This function retrieves the incident value from a tuple containing neighborhood data.
    Args:
        `item` (tuple): A tuple where the first element is the neighborhood name and the second element is a list
                        containing the number of incidents and confidence level.
    Returns:
        `int`: The number of incidents for the neighborhood.
    """
    selected_data = item[1][0]
    return selected_data
