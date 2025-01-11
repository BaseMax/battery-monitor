import psutil

def get_battery_info():
    battery = psutil.sensors_battery()

    if battery is None:
        return "No battery information available"

    battery_info = {
        'Percent': battery.percent,
        'Plugged In': battery.power_plugged,
        'Time Left': battery.secsleft if battery.secsleft != psutil.POWER_TIME_UNLIMITED else "Charging",
        'Charging': battery.power_plugged,
        'Battery Health': battery.percent >= 80,
        'Current Charge': battery.percent,
        'Battery Time Left (seconds)': battery.secsleft,
    }

    return battery_info


battery_info = get_battery_info()
print(battery_info)
