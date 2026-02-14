from system.hardware_profiler import build_profile
from system.capability_analyzer import analyze
from system.question_engine import ask_robot_config


def main():
    print("Scanning hardware...")
    profile = build_profile()

    print("Analyzing capabilities...")
    capabilities = analyze(profile)

    print("Robot configuration required.")
    robot_config = ask_robot_config()

    print("\n=== HARDWARE PROFILE ===")
    print(profile)

    print("\n=== CAPABILITIES ===")
    print(capabilities)

    print("\n=== ROBOT CONFIG ===")
    print(robot_config)


if __name__ == "__main__":
    main()