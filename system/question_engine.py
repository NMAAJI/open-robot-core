def _ask_positive_float(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if value <= 0:
                print("Value must be greater than 0.")
                continue
            return value
        except ValueError:
            print("Please enter a numeric value in meters (example: 0.15).")


def ask_robot_config():
    config = {}

    wheel_diameter = _ask_positive_float("Wheel diameter (meters): ")
    if wheel_diameter > 2:
        print("Warning: wheel diameter looks very large. Confirm units are meters.")

    wheel_base = _ask_positive_float("Wheel base distance (meters): ")
    if wheel_base > 3:
        print("Warning: wheel base looks very large. Confirm units are meters.")

    config["wheel_diameter"] = wheel_diameter
    config["wheel_base"] = wheel_base
    config["motor_driver"] = input("Motor driver type (PWM/UART/CAN): ").strip()

    return config
