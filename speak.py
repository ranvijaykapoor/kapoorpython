from gtts import gTTS

from playsound import playsound
def speak_text(path_audio):
    playsound(path_audio)


def save_audio(text):
    tts = gTTS(text)
    tts.save('machali.mp3')
    print("audio file generated  ")
    speak_text('machali.mp3')

save_audio(" aaj  din bhar barish hui hai aur aaj mandesh ne khub machali mara hai lekin pani band kar ke mandesh aur bholu ne milakar aaj tabahi machai hai ")