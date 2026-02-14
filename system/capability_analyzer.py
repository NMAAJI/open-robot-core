def analyze(profile):
    capabilities = {}

    ram = str(profile.get("ram", ""))
    architecture = str(profile.get("architecture", ""))

    if "16G" in ram:
        capabilities["vision_enabled"] = True
        capabilities["slam_enabled"] = True
    else:
        capabilities["vision_enabled"] = False
        capabilities["slam_enabled"] = False

    if "aarch64" in architecture:
        capabilities["arm_optimized"] = True
    else:
        capabilities["arm_optimized"] = False

    return capabilities