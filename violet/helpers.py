import platform

opsys = f"{platform.system().replace('Darwin', 'MacOS')} {platform.machine()}"
