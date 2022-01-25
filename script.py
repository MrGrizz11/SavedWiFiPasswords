import subprocess
import re

command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()

profile_names = re.findall("All User Profile     : (.*)\r", command_output)

for name in profile_names:
    try:
        command_output = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()
        password = re.findall("Key Content            : (.*)\r", command_output)
        if password == []:
            print(name + ": None")
        else:
            print(name + ":", password[0])
    except:
        pass

from time import sleep
sleep(10)