# Traffic Light Simulator

## Requirements

- Python 3.6 or higher. Download from the official [python.org](https://www.python.org/downloads/).

## Installation

- Create a python virtual env: `python3 -m venv .venv`. See official [docs](https://docs.python.org/3/library/venv.html) for more info.
- Activate the virtual env.
- Install the package: `pip install -e .`

## Instructions

- The app can be run using the `trafficlight` command. Run `trafficlight -h` for instructions.
- Pass three aruguments to the command line for green, yellow and red light timers in seconds. `trafficlight 3 1 2`
- The app can be stopped using `Ctrl-C`

## Tests

- Install the test package: `pip install -e .[test]` 
- Run the test from the app root directory: `pytest -v`