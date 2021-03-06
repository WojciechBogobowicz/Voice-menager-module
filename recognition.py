import pyaudio,os
import speech_recognition as sr
import queue


class VoiceTranslator:
    def __init__(self, language='pl'):
        self._r = sr.Recognizer()
        self._mic = sr.Microphone()
        self._audios = queue.Queue()
        self._language=language
    
    def listen(self):
        with self._mic as source:
            self._r.adjust_for_ambient_noise(source)
            self._audios.put(self._r.listen(source))
    
    def process_audios(self):
        results = []
        while not self._audios.empty():
            results.append(self._process_audio())
        return results

    def _process_audio(self):
        try:
            audio=self._audios.get()
            recognition_result = self._r.recognize_google(audio, language=self._language)
        except:
            recognition_result = None
        return recognition_result

    
    def listen_and_translate_to_text(self):
        self.listen()
        return self._process_audio()


if __name__=="__main__":
    new_task = VoiceTranslator()
    #print("start recording")
    #new_task.listen()
    #print("stop recording")
    #print(*new_task.process_audios())
    print("start recording")
    t = new_task.listen_and_translate_to_text()
    print("stop recording")
    print(t)