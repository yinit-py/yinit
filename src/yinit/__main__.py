import time


def sigint_handler():
    print("SIGINT received! Running cleanup...")
    # Your custom logic here (e.g., close files, de-initialize peripherals)

try:
    # Your main program loop
    while True:
        print("Running...")
        time.sleep(30)
except KeyboardInterrupt:
    sigint_handler()
