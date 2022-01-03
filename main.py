import os
import sys
import time
import json
import tkinter as tk
import urllib3


if sys.platform == "win32":
    print("Some features are not supported on Windows")
    print("Please use Linux or MacOS")
    print("No support will be provided for Windows. Please use WSL, Linux or MacOS")
    platformsupport = False
elif sys.platform == "darwin":
    print("MacOS detected")
    platformsupport = True
elif sys.platform == "linux":
    print("Linux detected")
    platformsupport = True
else:
    print("Platform not supported.")
    print("No support will be provided for " + sys.platform)
    platformsupport = False


def help():
    print("""
    Commands:
    help - Prints this help message
    python_info - Prints information about the python interpreter
    get_system_info - Prints information about the system
    get_system_info_json - Prints information about the system in json format
    get_system_info_pretty - Prints information about the system in pretty format
    get_ip - Prints the IP address of the system
    get_mac - Prints the MAC address of the system
    get_os - Prints the operating system of the system
    get_uptime - Prints the uptime of the system
    get_cpu_usage - Prints the CPU usage of the system
    get_ram_usage - Prints the RAM usage of the system
    get_disk_usage - Prints the disk usage of the system
    shutdown - Shuts down the system
    reboot - Reboots the system
    dynamicimport - Dynamically imports a module
    get_python_info - Prints information about the python interpreter
    python_shell - Starts a python shell
    python_version - Prints the python version
    python_version_info - Prints the python version info
    python_implementation - Prints the python implementation

    """)
# Define the commands
def shell_exec(cmd):
    return os.popen(cmd).read().strip()

def get_ip():
    if platformsupport:
        return shell_exec("hostname -I | awk '{print $1}'")
    else:
        return("Platform not supported.")

def get_mac():
    if platformsupport:
        return shell_exec("cat /sys/class/net/eth0/address")
    else:
        return("Platform not supported.")

def get_os():
    return sys.platform

def get_uptime():
    if platformsupport:
        return shell_exec("uptime -p")
    else:
        return("Platform not supported.")

def get_cpu_usage():
    if platformsupport:
        return shell_exec("top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'")
    else:
        return("Platform not supported.")

def get_ram_usage():
    if platformsupport:
        return shell_exec("free -m | awk 'NR==2{printf \"RAM: %s/%sMB (%s%%)\", $3,$2,$3*100/$2 }'")
    else:
        return("Platform not supported.")

def get_disk_usage():
    if platformsupport:
        return shell_exec("df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB (%s)\\n\", $3,$2,$5}'")
    else:
        return("Platform not supported.")

def dynamicimport(module):
    return __import__(module)

def python_version():
    return sys.version

def python_version_info():
    return sys.version_info

def python_implementation():
    return sys.implementation

def python_shell():
    print("Python shell started.")
    print("Type exit to exit the shell.")
    while True:
        try:
            cmd = input(">>> ")
            if cmd == "exit":
                break
            else:
                exec(cmd)
        except KeyboardInterrupt:
            print("\n")
            continue
        except Exception as e:
            print(e)

def python_info():
    return {
        "python_version": python_version(),
        "python_version_info": python_version_info(),
        "python_implementation": python_implementation()
    }

def get_python_info():
    return json.dumps(python_info(), indent=4)

def shutdown():
    if platformsupport:
        os.system("sudo shutdown -h now")
    else:
        print("Platform not supported.")

def reboot():
    if platformsupport:
        os.system("sudo reboot")
    else:
        print("Platform not supported.")

def get_system_info():
    return {
        "ip": get_ip(),
        "mac": get_mac(),
        "os": get_os(),
        "uptime": get_uptime(),
        "cpu_usage": get_cpu_usage(),
        "ram_usage": get_ram_usage(),
        "disk_usage": get_disk_usage()
    }

def get_system_info_json():
    return json.dumps(get_system_info(), indent=4)

def get_system_info_pretty():
    return json.dumps(get_system_info(), indent=4, sort_keys=True)

def windows_support_notice():
    print("""Windows uses a different command line interface. This command line interface cannot do everything that the CLI on Linux and MacOS can do.
    Please Use WSL, Linux or MacOS. *NO SUPPORT WILL BE PROVIDED FOR WINDOWS*""")

def duckduckgo_answers(query):
    http = urllib3.PoolManager()
    r = http.request('GET', 'https://api.duckduckgo.com/?q=' + query + '&format=json&pretty=1')
    return json.loads(r.data.decode('utf-8'))

def duckduckgo_answers_pretty(query):
    return json.dumps(duckduckgo_answers(query), indent=4, sort_keys=True)

def duckduckgo_answers_json(query):
    return json.dumps(duckduckgo_answers(query))

def clear():
    if sys.platform == "win32":
        os.system("cls")
    elif sys.platform == "darwin" or sys.platform == "linux":
        os.system("clear")
    else:
        print("Platform not supported.")

def cls():
    if sys.platform == "win32":
        os.system("cls")
    elif sys.platform == "darwin" or sys.platform == "linux":
        os.system("clear")
    else:
        print("Platform not supported.")
    





class Experimental:
    def __init__(self):
        print("NOTE: Experimental features are still under heavy development.")
        print("Please use with caution.")
    def gui(self):
        self.root = tk.Tk()
        self.root.title("Experimental")
        self.root.geometry("300x300")
        self.root.resizable(False, False)
        self.root.configure(background="#000000")
        self.root.mainloop()
        # Add the commands to the GUI
        
            
        



class Debug():
    def __init__(self):
        self.debug = True
        self.debug_print = True
        self.debug_time = True
        self.debug_json = True
        self.debug_pretty = True
        self.debug_time_start = time.time()
        self.debug_time_end = time.time()
        self.debug_time_total = time.time()
    
    def check_debug_enabled(self):
        if self.debug is False:
            self.debug_print = False
            self.debug_json = False
            self.debug_pretty = False
            self.debug_time = False

    def debug_disabled(self, debugtype):
        if debugtype:
            print("Debugging is disabled for " + debugtype)
        else:
            print("Debugging is disabled")
            print("Please enable debugging for this feature")
    def print(self, msg):
        if self.debug_print:
            print(msg)
        else:
            self.debug_disabled("print")
    def time(self, msg, code):
        if self.debug_time:
            time1 = time.gmtime()
            eval(code)
            return time.gmtime - time1
        else:
            self.debug_disabled("time")
    def json(self, msg):
        if self.debug_json:
            print(json.dumps(msg, indent=4))
        else:
            self.debug_disabled("json")
    def pretty(self, msg):
        if self.debug_pretty:
            print(json.dumps(msg, indent=4, sort_keys=True))
        else:
            self.debug_disabled("pretty")
    def time_start(self, msg):
        if self.debug_time:
            self.debug_time_start = time.gmtime()
        else:
            self.debug_disabled("time")
    def time_end(self, msg):
        if self.debug_time:
            self.debug_time_end = time.gmtime()
            self.debug_time_total = self.debug_time_end - self.debug_time_start
            print(msg + ": " + str(self.debug_time_total))
        else:
            self.debug_disabled("time")
    def time_total(self, msg):
        if self.debug_time:
            self.debug_time_total = self.debug_time_end - self.debug_time_start
            print(msg + ": " + str(self.debug_time_total))
        else:
            self.debug_disabled("time")

    def set_debug(self, debug):
        self.debug = debug
        if self.debug:
            self.debug_print = True
            self.debug_time = True
            self.debug_json = True
            self.debug_pretty = True
        else:
            self.debug_print = False
            self.debug_time = False
            self.debug_json = False
            self.debug_pretty = False


# If the script is not imported, run a frontend
if __name__ == "__main__":
    # Create a custom REPL
    command = input(">>> ")
    while command != "exit":
        try:
            exec(command + "()")
        except NameError:
            print(shell_exec(command))
        except BaseException as e:
            print(e)
        command = input(">>> ")
    print("Exiting...")
    sys.exit(0)



# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# EOF
