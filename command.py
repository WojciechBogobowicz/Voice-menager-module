from os import access
from ssl import SSL_ERROR_EOF
from recognition import VoiceTranslator
from ui import BinderUI, ConsoleUI
from action import Action


class ActionBinder:
    def __init__(self, voice_translator: VoiceTranslator, ui: BinderUI, aliases: dict()) -> None:
        self.aliases = aliases
        self._current_alias = None
        self.translator = voice_translator
        self.ui = ui
        self._saved_aliases_to_func = dict()
        self._read_save()

    def bind_action(self, fucntion, *args, **kwargs):
        action = Action(fucntion, *args, **kwargs)
        action_func_name = action.function.__name__
        if action_func_name in self._saved_aliases_to_func.values():
            self._add_saved_actions(action)
        else:
            self._bind_new_action(action)

    def _add_saved_actions(self, action: Action):
        action_name = action.function.__name__
        for alias, func_name in self._saved_aliases_to_func.items():
            if func_name == action_name:
                self.aliases[alias] = action

    def _bind_new_action(self, action: Action):
        self.ui.first_record(action.function.__name__)
        self._add_alias(action)
        self.ui.end_record()
        reminding_records = 2
        while reminding_records > 0:
            self.ui.next_record(reminding_records)
            alias_status = self._add_alias(action)
            self.ui.end_record()
            if alias_status == "new" or alias_status == 'undefined':
                self.ui.cannot_recoginze_message()
                reminding_records += 2
            elif alias_status == "old":
                self.ui.recoginzed_succesly_message()
                reminding_records -=1
        self.ui.action_added_message()

    def _add_alias(self, action: Action):
        self._set_current_alias()
        self._check_conflicts_with_other_actions(action)
        status = self._decide_if_alias_is_new()
        self._bind_alias_to_action(action)
        self._save_alias(action, status)
        self._clear_current_alias()
        return status

    def _set_current_alias(self):
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
        elif alias == None:
            alias_status = 'undefined'
        else:
            alias_status = "new"
        return alias_status

    def _bind_alias_to_action(self, action: Action):
        self.aliases[self._current_alias] = action
    
    def _save_alias(self, action: Action, status):
        if status == "new":
            func_name = action.function.__name__
            line = self._current_alias + ';' + func_name + "\n"
            with open('save.txt', 'a') as f:
                f.write(line)

    def _clear_current_alias(self):
        self._current_alias = ''

    def _read_save(self):
        with open('save.txt', 'r') as f:
            for line in f:
                alias, func_name = line.split(';')
                self._saved_aliases_to_func[alias]=func_name.strip()
                

class ActionExecuter:
    def __init__(self, translator: VoiceTranslator, aliases: dict) -> None:
        self.aliases = aliases
        self.translator = translator
    
    def _execute(alias):
        pass
    


if __name__=="__main__":
    def hello_world(kto_wita, kwarg1, kwarg2):
        print("cześć świecie od", kto_wita)

    def goodbye_world():
        print("its time")    


    aliases = dict()
    vt = VoiceTranslator()
    ui = ConsoleUI()
    cm = ActionBinder(vt, ui, aliases)
    cm.bind_action(hello_world, 'Martyna', kwarg1 = 1, kwarg2 = 2)
    cm.bind_action(goodbye_world)
    #saver = ActionStreamer(aliases)
    #saver.save()

    print(cm.aliases)

