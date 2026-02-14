from system.hardware_profiler import build_profile
from system.capability_analyzer import analyze
from system.question_engine import ask_robot_config


def print_section(title, data):
    print(f"\n=== {title} ===")
    if not data:
        print("(empty)")
        return

    key_width = max(len(str(key)) for key in data.keys())
    for key, value in data.items():
        print(f"{str(key):<{key_width}} : {value}")


def main():
    print("Scanning hardware...")
    profile = build_profile()

    print("Analyzing capabilities...")
    capabilities = analyze(profile)

    print("Robot configuration required.")
    robot_config = ask_robot_config()

    print_section("HARDWARE PROFILE", profile)
    print_section("CAPABILITIES", capabilities)
    print_section("ROBOT CONFIG", robot_config)


if __name__ == "__main__":
    main()
