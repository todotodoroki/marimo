def read_temperature():
    # This function simulates reading the temperature from a sensor.
    # Replace this with actual sensor reading code.
    import random
    return round(random.uniform(15.0, 30.0), 2)

def get_temperature():
    # This function retrieves the current water temperature.
    temperature = read_temperature()
    return temperature