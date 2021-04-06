import os
from io import BytesIO
from gtts import gTTS
from pydub.playback import play
from pydub import AudioSegment


class Speaker:
    def __init__(self, language='pl') -> None:
        self.language = language

    def speak(self, text):
        if text == "***** ***":
            text = "jebać pis"
        # get audio from server
        tts = gTTS(text=text, lang=self.language)
        # convert to file-like object
        fp = BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        # play
        message = AudioSegment.from_file(fp, format="mp3")
        play(message)
        
    def save(self, text, file_name, extention='mp3'):
        tts = gTTS(text=text, lang=self.language)
        path = os.path.join('audios', f'{file_name}.{extention}')
        tts.save(path)

    def read_from_file(self, audio_name, extention='mp3', dir_path='audios'):
        path = os.path.join(dir_path, f'{audio_name}.{extention}')
        file = AudioSegment.from_file(file=path, format=extention)
        play(file)



if __name__=="__main__":
    from random import choice

    samples_str = """Accel World, Akudama Drive, Appare Ranman, Arifureta, Assassins Pride, Black Clover, Bleach, Clannad, Code Geass, Danmachi, Darwin's Game, Decadence, Dr. Stone, Eden's Zero, Enen no Shouboutai, Fairy Tail, Gintama, Gleipnir, Hachinan, HunterxHunter, Infinite Dendrogram, Jujutsu Kaisen, Kami no Tou, Kenja no Mago, Kill la Kill, Kimetsu no Yaiba, Kimisen, Kyokou Suiri (In/Spectre), Log Horizon, Magi, Naruto, No game no life, One Piece, Plunderer, Re:Zero, Saga Winlandzka, Shinchou Yuusha, Shingeki no Kyojin, Somali to Mori no Kamisama, Suisei no Gargantia, Sword Art Online, Tate no Yuusha no Nariagari, Tensei Shitara Slime Datta Ken, The God of High School, Yakusoku no Neverland, Pozostałe serie."""
    samples = samples_str.split(',')
    winner = choice(samples)

    dla_martynki = """
    To jasne, że wodorosty,
Najlepsze u obcych są.
Chcesz przenieść się tam na górę,
Lecz wielki popełniasz błąd.
Rozejrzyj się wokół siebie,
Bo tutaj na morza dnie,
Cudownie jest proszę ciebie.
Gdzie lepiej być może, gdzie?
Na morza dnie, na morza dnie,
Bo tam gdzie sucho,
Może być krucho,
Posłuchaj mnie!
Oni na górze, uwierz mi,
W słońcu harują całe dni.
My tylko jemy i dryfujemy,
Na morza dnie!
Szczęśliwe są wolne ryby,
Gdy kręcą się pośród fal.
W akwarium zza szklanej szyby,
Ze smutkiem zerkają w dal.
Lecz w sumie akwarium takie,
To nie jest najgorszy los.
Gdy zeżre ją ktoś ze smakiem,
"Tak to jest dla ryby cios".
A więc!
Na morza dnie, na morza dnie,
Nikt nas nie siecze,
Ani nie piecze,
A później je.
Wiedząc, że ludzie chcą nas tak,
Likwidujemy każdy hak.
I spokój… """
    #dla_martynki = 'test'
    s = Speaker()
    s.save(f"Cześć, jestem Tomek.", 'test')

    #s.speak(dla_martynki)
    #s.read_from_file('test')