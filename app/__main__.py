import signal
import time
import sys
import argparse

from app.trafficlight import TrafficLight, TrafficLightControl

from colorama import init

init(autoreset=True)

# store the original SIGINT handler
original_sigint = signal.getsignal(signal.SIGINT)


def signal_handler(signum, frame):
    signal.signal(signal.SIGINT, original_sigint)

    try:
        if input("\nQuit? (y/n)> ").lower().startswith("y"):
            print("Exiting Traffic Light Simulator")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\nExiting Traffic Light Simulator")
        sys.exit(1)

    # restore the signal handler here
    signal.signal(signal.SIGINT, signal_handler)


def run(*timers):
    light = TrafficLight()
    control = TrafficLightControl(light, timers)
    control.run()


def main():
    signal.signal(signal.SIGINT, signal_handler)
    parser = argparse.ArgumentParser(
        description="Welcome to the Traffic Light Simulator"
    )
    parser.add_argument("green", type=int, help="Green light timer in seconds")
    parser.add_argument("yellow", type=int, help="Yellow light timer in seconds")
    parser.add_argument("red", type=int, help="Red light timer in seconds")
    args = parser.parse_args()
    run(args.green, args.yellow, args.red)


if __name__ == "__main__":
    main()
