import json
import platform
import subprocess


def run(cmd):
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            check=False,
            timeout=5,
        )
        if result.returncode != 0:
            return ""
        return result.stdout.strip()
    except Exception:
        return ""


def is_linux():
    return platform.system().lower() == "linux"


def detect_model():
    try:
        if not is_linux():
            return "Unknown"
        model = run("cat /sys/firmware/devicetree/base/model")
        cleaned = model.replace("\x00", "").strip()
        return cleaned if cleaned else "Unknown"
    except Exception:
        return "Unknown"


def detect_cpu():
    if not is_linux():
        return ""
    return run("lscpu | grep 'Model name'")


def detect_arch():
    arch = run("uname -m")
    if arch:
        return arch
    return platform.machine()


def detect_ram():
    if not is_linux():
        return 0
    mem = run("free -g | awk '/Mem:/ {print $2}'")
    try:
        return int(mem)
    except (TypeError, ValueError):
        return 0


def detect_usb():
    if not is_linux():
        return ""
    return run("lsusb")


def detect_cameras():
    if not is_linux():
        return ""
    return run("v4l2-ctl --list-devices")


def detect_i2c():
    if not is_linux():
        return ""
    return run("ls /dev/i2c-* 2>/dev/null")


def detect_spi():
    if not is_linux():
        return ""
    return run("ls /dev/spidev* 2>/dev/null")


def detect_uart():
    if not is_linux():
        return ""
    return run("ls /dev/ttyUSB* 2>/dev/null")


def build_profile():
    profile = {
        "model": detect_model(),
        "cpu": detect_cpu(),
        "architecture": detect_arch(),
        "ram": detect_ram(),
        "usb_devices": detect_usb(),
        "camera_devices": detect_cameras(),
        "i2c_buses": detect_i2c(),
        "spi_buses": detect_spi(),
        "uart_devices": detect_uart(),
    }
    return profile


if __name__ == "__main__":
    profile = build_profile()
    print(json.dumps(profile, indent=4))
