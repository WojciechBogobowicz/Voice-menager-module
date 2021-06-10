# Voice menager module
**English version below:**  
Moduł ten został stworzony, żeby umożliwić użytkownikowi komunikację głosową z komputerem.
Głównymi załozeniami projektu są:
  - Stworzenie komputerowi możliwości mówienia.
  - Interpretowanie mowy ludzkiej
  - Nasłuchiwanie i wykonywanie komand glosowych.

Możesz wykorzystać ten moduł np do tworzenia smart domu.  
Rozpoznawanie mowy jest realizowane przy pomocy Google Translate, więc program wymaga stałego dotępu do internetu, żeby działał.  
Wszystkie komendy które program ma rozpoznawać powinny być dodane funkcją bind_action z klasy VoiceMenger, zanim rozpocznie się nasłuchiwanie. Jeśli program napotka na nowo zbindowaną funkcję to poprosi o kilkukrotne powtórzenie słownej komendy która powinna ją wywoływać. Funkcje do których już raz przypisno komendy, będą z nich korzystały przy kolejnych uruchomieniach bez konieczności pownego ich bindowania.  
UI dodawania komend jest klasą abstrakcyjną, więc uzytkownik może zdefiniować sobie swoją własną wersję.

--------------------------------------

**English:**  
This module is created to make voice comunication with computer easier.  
Main goals of this program are: 
  - Give to the computer speaking possibility 
  - Interpret human speach 
  - Listen for and execute programmist's voice command 

So you can use it, for example to build smart house.  
Speech recognition is based on Google Translate so it needs internet connection to work.  
All commands that program has to recogize, should be added by function bind_action from class VoiceMenager, before module start lisen for command. If program encounters freshly bound fucntion, then it will ask fiew times for a voice command which should be asociated with this function. Functions which already have binded commands, would use them in future runs without the need to bind them again.  
UI for adding commands is an abstract class, so  the user can define their own version. 
