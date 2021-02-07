from abc import ABC, abstractmethod


class CommandUI(ABC):
    @abstractmethod
    def first_record(self) -> None:
        pass

    @abstractmethod
    def next_record(self, reminding_records) -> None:
        pass

    @abstractmethod
    def end_record(self, record_is_recoginzed: bool) -> None:
        pass

    @abstractmethod
    def cannot_recoginze_message(self) -> None:
        pass

    @abstractmethod
    def recoginzed_succesly_message(self) -> None:
        pass

    @abstractmethod
    def action_added_message(self) -> None:
        pass


class ConsoleUI(CommandUI):
    def first_record(self):
        print("Your command record is starting. Please wait 2-3 secound and talk.")
    
    def next_record(self, reminding_records) -> None:
        print(f'You still have to record {reminding_records} times.')
        print("Your command record is starting. Please wait 2-3 secound and talk.")
    
    def end_record(self) -> None:
        print("Record ended")

    def cannot_recoginze_message(self) -> None:
        print('Your speech was to diffrent from the previous ones, so '
        'I have to record you more time.')

    def recoginzed_succesly_message(self) -> None:
        print('Everything went good.')

    def action_added_message(self) -> None:
        print('Action added.')

if __name__ == '__main__':
    pass
    x = ConsoleUI()