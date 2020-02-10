import time
import sys
import os

from colorama import Fore, Style


class TrafficLight:
    """
        Traffic light implementation
        2 = red
        1 = yellow
        0 = green
    """

    def __init__(self):
        self.light = ["#", " ", " "]
        self.current_light = 0
        self.max_light = len(self.light) - 1

    def change_light(self):
        self.light = [" ", " ", " "]
        self.current_light = (
            0 if self.current_light == self.max_light else self.current_light + 1
        )
        self.light[self.current_light] = "#"

    def show(self):
        r = (Fore.RED + self.light[2] * 4) + Style.RESET_ALL
        y = (Fore.YELLOW + self.light[1] * 4) + Style.RESET_ALL
        g = (Fore.GREEN + self.light[0] * 4) + Style.RESET_ALL

        print(
            f"""
      ##
     _[]_
    [____]
.----'  '----.
|    .==.    |
|   /{r}\   |
|   \{r}/   |
|    .==.    |
|    .==.    |
|   /{y}\   |
|   \{y}/   |
|    .==.    |
|    .==.    |
|   /{g}\   |
|   \{g}/   |
|    .==.    |
'--.______.--'
"""
        )


class TrafficLightControl:
    def __init__(self, traffic_light, timers):
        self.traffic_light = traffic_light
        self.light_timer = timers

    def run(self):
        while True:
            # Clear screen based on Windows or Mac/Linux
            os.system("cls" if os.name == "nt" else "clear")
            print("Ctrl-C to quit")
            self.traffic_light.show()
            time.sleep(self.light_timer[self.traffic_light.current_light])
            self.traffic_light.change_light()
