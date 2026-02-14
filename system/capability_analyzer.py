def analyze(profile):
    capabilities = {}

    ram_gb = profile.get("ram", 0)
    arch = profile.get("architecture", "")

    capabilities["arm_optimized"] = "aarch64" in arch

    if ram_gb >= 8:
        capabilities["vision_enabled"] = True
        capabilities["slam_enabled"] = True
        capabilities["nav2_enabled"] = True
    elif ram_gb >= 4:
        capabilities["vision_enabled"] = False
        capabilities["slam_enabled"] = True
        capabilities["nav2_enabled"] = True
    else:
        capabilities["vision_enabled"] = False
        capabilities["slam_enabled"] = False
        capabilities["nav2_enabled"] = False

    return capabilities
