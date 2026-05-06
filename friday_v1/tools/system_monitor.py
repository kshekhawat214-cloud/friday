import psutil
import time

from interface.text_to_speech import speak


def monitor_system():

    while True:

        battery = psutil.sensors_battery()

        if battery:
            if battery.percent < 20 and not battery.power_plugged:
                speak("Battery is below 20 percent")

        cpu = psutil.cpu_percent(interval=1)

        if cpu > 90:
            speak("CPU usage is very high")

        time.sleep(60)