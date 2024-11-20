import serial, time, os

curr_time = time.time()

def read_from_port(port):
    ser = serial.Serial(port, 115200, timeout=1)
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            current_time = time.localtime()
            formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
            print(f"[{formatted_time}]: {line}")
            save_logs(f"[{formatted_time}]: {line}\n")

def save_logs(log):
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)
    file_path = os.path.join(log_dir, f"{curr_time}.txt")
    with open(file_path, 'a') as f:
        f.write(log)

if __name__ == '__main__':
    port = input("Enter the port name: ")
    save_logs(f"Start logging at port: {port}")
    read_from_port(port)
