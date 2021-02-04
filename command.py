from recognition import VoiceManager


class Command:
    def __init__(self, name, action, *args):
        self.name = name
        self.action = action
        self.action_args = args

    def execute(self):
        self.action(*self.action_args)

    def execute_and_return(self):
        return self.action(*self.action_args)


class VoiceCommand(Command):
    def __init__(self, name, voice_manager, action, *args) -> None:
        super().__init__(name, action, *args)
        self.aliases = []
        self.voice_manager = voice_manager

    def _set_aliases(self, max_records = 10):
        remindig_records = 1
        while remindig_records < 0:
            audio = self.voice_manager.listen()
            alias = audio.process_audios()[0]
            if alias in self.aliases:
                remindig_records-=1
                self.aliases.append(alias)
            else:
                remindig_records+=2

            if remindig_records >= max_records:
                self.aliases = []
                return None
            
    def _aliases_are_set(self):
        return not self.aliases == []    

    def bind_command(self, max_records = 10):
        self._set_aliases(max_records)
        if not self._aliases_are_set():
            raise Exception("Voice command is too complicated. Maybe try to set something easier")



if __name__=="__main__":
    #def hello_world(kto_wita):
    #    print("cześć świecie od", kto_wita)

    #m = VoiceManager()
    #c = VoiceCommand("test", m, hello_world, "martynka")
    #c.set_aliases()
    #print(c.aliases)
