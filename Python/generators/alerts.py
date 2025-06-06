def alert_generator(risk_value):
    if risk_value == 0:
        return "No risk detected. Enjoy your day!"
    elif risk_value == 1:
        return "Low risk detected. Stay alert!"
    elif risk_value == 2:
        return "Moderate risk detected. Take precautions!"
    elif risk_value == 3:
        return "High risk detected. Evacuate if necessary!"
    elif risk_value == 4:
        return "Extreme risk detected! Immediate action required!"
    else:
        return "Invalid risk value."