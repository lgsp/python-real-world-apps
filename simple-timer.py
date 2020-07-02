import os
import time
import datetime
import playsound


class Alarm(object):
    def __init__(self):
        self.current_time = str(datetime.datetime.fromtimestamp \
                                (time.time()).strftime('%H:%M:%S'))

    def __repr__(self):
        mins = int(self.clock())
        print(self.set_to(mins))
        self.alarm(mins)

    def clock(self):
        print(f"\n\t[ ALARM ]\nCurrent Time: {self.current_time}")
        try:
            minutes = int(input("Minutes: "))
        except:
            print("Invalid Data!")
            self.clock()
        return minutes

    def set_to(self, minutes):
        notification = self.current_time.split(":")
        hour = int(notification[0])
        mins = int(notification[1])
        secs = int(notification[2])
        if 0 < mins + minutes < 60:
            mins += minutes
        else:
            hour += minutes // 60
            mins += minutes % 60
        return str(f"Alarm set to: {hour}:{mins}:{secs}")

    def alarm(self, mins):
        time.sleep(mins * 60)
        frequency = 2500 # 2500 Hz
        duration = 1000 # 1 sec
        playsound.Beep(frequency, duration)


if __name__ == "_main__":
    Alarm().__repr__()
