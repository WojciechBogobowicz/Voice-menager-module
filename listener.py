from command import ActionBinder
from recognition import VoiceTranslator
from ui import ConsoleUI
from speaker import Speaker

class Listener:
    def __init__(self, wakeup_aliases: tuple, aliases_to_actions: dict, translator: VoiceTranslator) -> None:
        self.alias_to_actions = aliases_to_actions
        self.translator = translator
        self.wakeup_aliases = wakeup_aliases
        self.speaker = Speaker()

    def start_listen(self):
        i = 1
        while True:
            text = self.translator.listen_and_translate_to_text()
            if text in self.wakeup_aliases:
                self.speaker.speak("W czym mogę pomóc?")
                alias = self.translator.listen_and_translate_to_text()
                if alias in self.alias_to_actions:
                    self.alias_to_actions[alias].execute()
                else:
                    self.speaker.speak("Przepraszam, nie zrozumiałem.")
                    print('Zarejstrowano:', alias)
            print(f"Usłyszałem {text}, wywoluje się {i}ty raz")
            i+=1


if __name__ == "__main__":
    def hello_world(kto_wita, kwarg1, kwarg2):
        print("cześć świecie od", kto_wita)

    def goodbye():
        s = Speaker()
        s.speak('Do usłyszenia')
        exit()

    aliases = dict()
    vt = VoiceTranslator()
    ui = ConsoleUI()
    cm = ActionBinder(vt, aliases)
    cm.bind_action(ui, goodbye)
    l = Listener(("Cześć Tomek", "Cześć Tomku" "Tomek", "Tomku"), cm.aliases, vt)
    l.start_listen()
