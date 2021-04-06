from command import ActionBinder
from recognition import VoiceTranslator
from ui import ConsoleUI
from speaker import Speaker
from listener import Listener
from functions import actual_commands, goodbye, current_time, light_off, light_on, love_you, tell_it
import serial


if __name__ == "__main__":
    serial_is_used_for_arduino = False
    if serial_is_used_for_arduino:
        ser = serial.Serial('/dev/ttyUSB0')
        

    aliases = dict()
    vt = VoiceTranslator()
    ui = ConsoleUI()
    cm = ActionBinder(vt, aliases)


    cm.bind_action(ui, goodbye)
    cm.bind_action(ui, current_time)
    cm.bind_action(ui, love_you)
    
    if serial_is_used_for_arduino:
        cm.bind_action(ui, light_on)
        cm.bind_action(ui, light_off)
    cm.bind_action(ui, actual_commands, aliases)
    cm.bind_action_mannualy(('Lustereczko powiedz przecie kto jest najpiękniejszy w świecie',), tell_it)

    l = Listener(("Cześć Tomek", "Cześć Tomku", "Tomek", "Tomku"), cm.aliases, vt)
    l.start_listen()


    if serial_is_used_for_arduino:
        ser.close()

    print("dokonało się")