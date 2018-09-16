import subprocess
results = subprocess.check_output(["netsh", "wlan", "show", "all"])
print results