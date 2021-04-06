from speaker import Speaker
from datetime import datetime
import serial


s = Speaker()

def goodbye(speaker: Speaker = s):
    print("Initializing self-destruction")
    speaker.speak('Do usłyszenia')
    exit()

def current_time(speaker: Speaker = s):
    speaker.speak(datetime.now().strftime("%H:%M"))

def love_you(speaker: Speaker = s):
    speaker.speak('Też Cię Kocham')

def tell_it(speaker: Speaker = s):
    speaker.speak("Martyna")

def actual_commands(commands: dict, speaker: Speaker = s):
    speaker.speak("Obecnie przypięte komendy to:")
    for alias, command in commands.items():
        speaker.speak(f"{alias} do funkcji {command.func.__name__}")

def light_on(ser: serial.Serial):
    ser.baudrate = 9600
    ser.write(b'1')

def light_off(ser: serial.Serial):
    ser.baudrate = 9600
    ser.write(b'0')


if __name__=='__main__':
    #current_time()
    print("Cześć Tomku" == "Cześć Tomku")
