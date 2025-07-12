
def read_temperature():
    # This function simulates reading the temperature from a sensor.
    # Replace this with actual sensor reading code.
    import random
    return round(random.uniform(15.0, 30.0), 2)

def read_temperature_real():
    # This function read real sensor value
    # Neeed hardawre
    from w1thermsensor import W1ThermSensor
    ds18b20_sensor = W1ThermSensor()
    temp = ds18b20_sensor.get_temperature()
    return round(temp, 2)

def get_temperature():
    # This function retrieves the current water temperature.
    temperature = read_temperature_real()
    return temperature
