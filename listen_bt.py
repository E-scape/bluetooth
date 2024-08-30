import serial
import time
import subprocess

def read_from_hc06(ser):
    print("Listening for data from HC-06...")
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').rstrip()
            print(f"Received: {data}")
            
            if data == "camera":
                subprocess.run(["python3", "/home/escape/escape_project/print.py"])
        time.sleep(1)

def main():
    bt_addr = "98:DA:60:07:C6:AC"
    ser = serial.Serial(
        port='/dev/rfcomm0',  # 변경해야 할 수 있음
        baudrate=9600,
        timeout=1
    )
    read_from_hc06(ser)

if __name__ == "__main__":
    main()