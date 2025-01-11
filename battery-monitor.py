import psutil
from termcolor import colored
import os
import platform


def clear_screen():
    """Clear the terminal screen based on the OS."""
    if platform.system() == "Windows":
        os.system('cls')
    elif platform.system() == "Darwin":
        os.system('clear')
    else:
        os.system('clear')


def get_battery_info():
    """Returns the battery status as a dictionary."""
    battery = psutil.sensors_battery()
    if battery is None:
        return {"Error": "No battery information available"}

    percent = battery.percent
    plugged_in = battery.power_plugged
    time_left = battery.secsleft if battery.secsleft != psutil.POWER_TIME_UNLIMITED else "Charging"
    charging = "Yes" if plugged_in else "No"
    health = "Healthy" if percent >= 80 else "Warning: Low Health"

    return {
        'Battery Percentage': f"{percent}%",
        'Plugged In': "Yes" if plugged_in else "No",
        'Charging': charging,
        'Time Left': f"{time_left // 60} minutes" if isinstance(time_left, int) else time_left,
        'Battery Health': health,
    }


def format_output(info):
    """Returns formatted colored output for battery info."""
    formatted_info = []
    for key, value in info.items():
        color = get_color(value)
        formatted_info.append(colored(f"{key}: ", "blue") + colored(value, color))
    return "\n".join(formatted_info)


def get_color(value):
    """Returns a color based on the value."""
    if "Healthy" in value or "Yes" in value:
        return "green"
    elif "Warning" in value:
        return "yellow"
    else:
        return "red"


def print_battery_info():
    """Prints the battery information with system info and formatted output."""
    clear_screen()

    os_info = f"{platform.system()} {platform.release()}"
    battery_info = get_battery_info()

    print(colored("=" * 30, "cyan"))
    print(colored("   Battery Monitor   ", "cyan"))
    print(colored("=" * 30, "cyan"))
    
    print(colored(f"System: {os_info}", "cyan"))
    print(colored(f"Machine: {platform.machine()}", "magenta"))
    print(colored(f"Processor: {platform.processor()}", "yellow"))
    print(colored("=" * 30, "cyan"))
    
    if "Error" in battery_info:
        print(colored(battery_info["Error"], "red"))
    else:
        print(format_output(battery_info))

    print(colored("=" * 30, "cyan"))
    print(colored("Powered by Battery Monitor (github.com/basemax)", "magenta"))


if __name__ == "__main__":
    print_battery_info()
