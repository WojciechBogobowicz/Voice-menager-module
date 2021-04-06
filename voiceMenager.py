from listener import Listener
from recognition import VoiceTranslator
from ui import ConsoleUI, BinderUI
from command import ActionBinder
from functions import actual_commands, goodbye, current_time, light_off, light_on, love_you, tell_it
import serial

class VoiceMenager:
    def __init__(self) -> None:
        self.aliases = dict()
        self.vt = VoiceTranslator()
        self.ab = ActionBinder(self.vt, self.aliases)
        self.l = Listener(("Cześć Tomek","Tomek", "Tomku"), 
                            self.ab.aliases, self.vt)
        try:
            self.ser = serial.Serial('/dev/ttyUSB0')
            self.serial_open = True
            print("ser opened", self.ser)
        except:
            self.ser=None
            self.serial_open = False 
    
    def __del__(self): 
        if self.serial_open:
            self.ser.close()
            print("ser closed")
        else:
            print("nothing to close")
        
    def start_listen(self):
        self.l.start_listen()

    def bind_action(self, ui: BinderUI, fucntion, *args, **kwargs):

        self.ab.bind_action(ui, fucntion, *args, **kwargs)
    


if __name__ == "__main__":
    ui = ConsoleUI()

    cm = VoiceMenager()
    cm.bind_action(ui, goodbye)
    cm.bind_action(ui, current_time)
    cm.bind_action(ui, love_you)
    cm.bind_action(ui, light_on, cm.ser)
    cm.bind_action(ui, light_off, cm.ser)
    cm.bind_action(ui, actual_commands, cm.aliases)

    
    cm.start_listen()
    