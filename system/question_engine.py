def ask_robot_config():
    config = {}

    config["wheel_diameter"] = input("Wheel diameter (meters): ")
    config["wheel_base"] = input("Wheel base distance (meters): ")
    config["motor_driver"] = input("Motor driver type (PWM/UART/CAN): ")

    return config