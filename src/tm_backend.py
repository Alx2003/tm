import sys
import psutil as psu

def send_message(data):
    sys.stdout.write("{:.2f}".format(data[0]))
    sys.stdout.flush()

def access_info():
    data = []

    # Gather data on performance
    cpu_percent = psu.cpu_percent(interval=1)
    data.append(cpu_percent)

    return data

def main():
    data = access_info()
    send_message(data)
    exit(0)

if __name__ == "__main__":
    main()