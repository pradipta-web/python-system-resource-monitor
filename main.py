import psutil
import platform
import socket
import os
import time
from datetime import datetime


def get_system_info():
    print("SYSTEM INFORMATION")
    print("-" * 50)

    print(f"Hostname        : {socket.gethostname()}")
    print(f"Operating System: {platform.system()}")
    print(f"Architecture    : {platform.architecture()[0]}")


def get_cpu_info():
    cpu_usage = psutil.cpu_percent(interval=None)

    print("\nCPU MONITORING")
    print("-" * 50)
    print(f"CPU Usage       : {cpu_usage}%")


def get_memory_info():
    memory = psutil.virtual_memory()

    total = memory.total / (1024 ** 3)
    used = memory.used / (1024 ** 3)
    available = memory.available / (1024 ** 3)

    print("\nMEMORY MONITORING")
    print("-" * 50)
    print(f"Total RAM       : {total:.2f} GB")
    print(f"Used RAM        : {used:.2f} GB")
    print(f"Available RAM   : {available:.2f} GB")
    print(f"RAM Usage       : {memory.percent}%")


def get_disk_info():
    disk = psutil.disk_usage("C:\\")

    total = disk.total / (1024 ** 3)
    used = disk.used / (1024 ** 3)
    free = disk.free / (1024 ** 3)

    print("\nDISK MONITORING")
    print("-" * 50)
    print(f"Total Disk      : {total:.2f} GB")
    print(f"Used Disk       : {used:.2f} GB")
    print(f"Free Disk       : {free:.2f} GB")
    print(f"Disk Usage      : {disk.percent}%")

def get_network_info(previous_net, previous_time):
    current_net = psutil.net_io_counters()
    current_time = time.time()

    elapsed = current_time - previous_time

    upload_speed = (current_net.bytes_sent - previous_net.bytes_sent) / elapsed
    download_speed = (current_net.bytes_recv - previous_net.bytes_recv) / elapsed

    print("\nNETWORK MONITORING")
    print("-" * 50)
    print(f"Total Uploaded   : {current_net.bytes_sent / (1024 ** 2):.2f} MB")
    print(f"Total Downloaded : {current_net.bytes_recv / (1024 ** 2):.2f} MB")
    print(f"Upload Speed     : {upload_speed / 1024:.2f} KB/s")
    print(f"Download Speed   : {download_speed / 1024:.2f} KB/s")

    return current_net, current_time


def main():
    psutil.cpu_percent(interval=None)

    previous_net = psutil.net_io_counters()
    previous_time = time.time()

    try:
        while True:
            os.system("cls" if os.name == "nt" else "clear")

            print("=" * 50)
            print("       REAL-TIME SYSTEM RESOURCE MONITOR")
            print("=" * 50)

            get_system_info()
            get_cpu_info()
            get_memory_info()
            get_disk_info()

            previous_net, previous_time = get_network_info(
                previous_net,
                previous_time
            )

            print("\n" + "=" * 50)
            print(f"Last Updated: {datetime.now().strftime('%H:%M:%S')}")
            print("Refresh Interval: 2 seconds")
            print("Press CTRL+C to stop monitoring.")
            print("=" * 50)

            time.sleep(2)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")


if __name__ == "__main__":
    main()