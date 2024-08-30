import subprocess
import time

def connect():
    subprocess.run("gnome-terminal -- bash -c 'sudo rfcomm connect escape 98:DA:60:07:C6:AC 1; exec bash'", shell=True)

def check():
    output = subprocess.check_output("hcitool con", shell=True, universal_newlines=True)
    
    if "98:DA:60:07:C6:AC" in output:
        return True
    else:
        print("reconnecting")
        return False
    
connect()
time.sleep(5)
subprocess.run("gnome-terminal -- bash -c 'python3 /home/escape/escape_project/listen_bt.py; exec bash'", shell=True)
time.sleep(1)

while True:
    if not check():
        connect()
        time.sleep(5)
        subprocess.run("pkill gnome-terminal", shell=True, check=True)

        if check() == True:    
            subprocess.run("gnome-terminal -- bash -c 'python3 /home/escape/escape_project/listen_bt.py; exec bash'", shell=True)
        else:
            continue

    time.sleep(10)