# TODO Test this on Windows

import platform
import subprocess

# Check the operating system
os_name = platform.system()

# Set the Discord binary path based on the operating system
if os_name == 'Windows':
    discord_path = 'C:\Program Files (x86)\Discord\Discord.exe'
elif os_name == 'Darwin':  # macOS
    discord_path = '/Applications/Discord.app/Contents/MacOS/Discord'
else:
    # Assume Linux
    discord_path = '/usr/bin/discord'

# Open Discord using the default binary path
subprocess.run([discord_path])
