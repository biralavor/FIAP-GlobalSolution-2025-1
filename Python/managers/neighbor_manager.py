from utils.finders import neighbor_risk_finder
from utils.finders import neighborhood_finder
from generators.alerts import alert_generator

def neighborhood_manager(user_type: str, user_location: str, data_with_rainfall: dict) -> int:
    neighbor = neighborhood_finder(user_location, data_with_rainfall)
    if neighbor:
        risk_value = neighbor_risk_finder(neighbor, data_with_rainfall)
        alert_generator(risk_value)
        if risk_value == 4:
            exit(0)
    else:
        risk_value = neighborhood_manager(user_type, user_location, data_with_rainfall)
    return risk_value