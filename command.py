from ssl import SSL_ERROR_EOF
from recognition import VoiceTranslator
from ui import CommandUI, ConsoleUI
from action import Action

class CommandMenager:
    def __init__(self, voice_translator: VoiceTranslator, ui: CommandUI) -> None:
        self.aliases = dict()
        self._current_alias = None
        self.translator = voice_translator
        self.ui = ui

    def add_action(self, fucntion, *args, **kwargs):
        action = Action(fucntion, *args, **kwargs)
        self.ui.first_record()
        self._add_alias(action)
        self.ui.end_record()
        reminding_records = 2
        while reminding_records > 0:
            self.ui.next_record(reminding_records)
            alias_status = self._add_alias(action)
            self.ui.end_record()
            if alias_status == "new" or self._current_alias == None:
                self.ui.cannot_recoginze_message()
                reminding_records += 2
            elif alias_status == "old":
                self.ui.recoginzed_succesly_message()
                reminding_records -=1
        self.ui.action_added_message()
            
    def _add_alias(self, action: Action):
        self._add_current_alias()
        self._check_conflicts_with_other_actions(action)
        status = self._decide_if_alias_is_new()
        self._bind_aliast_to_action(action)
        self._clear_current_alias()
        return status

    def _add_current_alias(self):
        alias = self.translator.listen_and_translate_to_text()
        self._current_alias = alias

    def _check_conflicts_with_other_actions(self, action: Action):
        alias = self._current_alias
        if alias in self.aliases:
            if not self.aliases[alias]==action:
                raise ValueError(f"Command is too similar to {str(self.aliases[alias])}")

    def _decide_if_alias_is_new(self):
        alias = self._current_alias
        if alias in self.aliases:
            alias_status = "old"
        else:
            alias_status = "new"
        return alias_status

    def _bind_aliast_to_action(self, action: Action):
        self.aliases[self._current_alias] = action
    
    def _clear_current_alias(self):
        self._current_alias = ''





if __name__=="__main__":
    def hello_world(kto_wita):
        print("cześć świecie od", kto_wita)

    #m = VoiceTranslator()
    #c = VoiceCommand("test", m, hello_world, "martynka")
    #c.set_aliases()
    #print(c.aliases)
    pass
    vt = VoiceTranslator()
    ui = ConsoleUI()
    cm = CommandMenager(vt, ui)
    cm.add_action(hello_world)
    print(cm.aliases)



"""

class Command:
    def __init__(self, fucntion, *args):
        self.fucntion = fucntion
        self.action_args = args

    def execute(self):
        self.fucntion(*self.action_args)

    def execute_and_return(self):
        return self.fucntion(*self.action_args)

    def __str__(self):
        return 'command for ' + self.fucntion.__name__


class VoiceCommand(Command):
    def __init__(self, name, voice_translator, fucntion, *args, **kwargs) -> None:
        super().__init__(name, fucntion, *args)
        self._aliases = CommandAliases()
        self._voice_translator = voice_translator

        self._start_record_notification = self._default_start_notification
        self._end_record_notification = self._default_end_notification

    def record(self):
        alias = self._voice_translator.listen_and_translate_to_text()
        self._aliases.add_alias(alias)

    def record_few_times(self, repeats):
        pass

    def record_until_no_new_aliases(self):
        pass

    def _default_start_notification(self):
        print("Record starting, please wait 2-3 sec and talk.")

    def _default_end_notification(self):
        print("Record end.")

    def _new_alias_notification(self):
        print("I processed your voice ")


    #@sound_effect




class CommandAliases:
    def __init__(self) -> None:
        self.aliases = set()

    def add_alias(self, alias):
        if len(self.aliases) >= 10:
            warnings.warn(f"Generated {len(self.aliases)} diffrent aliases for this command. Maybe clean those, and try to choose easier command")
        self.aliases.append(alias)

    def is_new_alias(self, alias):
        return alias not in self.aliases

    def delete_all(self):
        self.aliases = []"""