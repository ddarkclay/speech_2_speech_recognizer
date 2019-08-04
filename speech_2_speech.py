import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak Anything : ')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('You Said : {}'.format(text))
        my_audio = gTTS(text)
        my_audio.save('my_audio.mp3')
        playsound('my_audio.mp3')

    except:
        print('Not Recognize your voice .')