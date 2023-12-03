# pip install SpeechRecognition
# pip install PyAudio
# pip install googletrans==4.0.0rc1
# pip install gTTS

import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

# create a recognizer and translator instance
r = sr.Recognizer()
translator = Translator(service_urls=['translate.google.co.il'])
language = 'el'

# use the default microphone as the audio source
with sr.Microphone() as source:
    if language == 'he':
        print("Speak something in Hebrew...")
    else:
        print("Speak something in Greek...")
    # listen for audio and convert it to text
    audio = r.listen(source)
    print(len(audio.get_raw_data()))
    # try:
    #     if language == 'he':
    #         # recognize speech using Google Cloud Speech Recognition with Hebrew language
    #         text = r.recognize_google(audio, language='he-IL') # Hebrew speech input
    #     else:
    #         # recognize speech using Google Cloud Speech Recognition with Hebrew language
    #         text = r.recognize_google(audio, language='el-GR') # Greek speech input
    #     if text:
    #         print("You said: " + text)
    #         # translate the text to English
    #         translation = translator.translate(text, src=language, dest='en')
    #         print("Translation: " + translation.text)
    #         # convert the text to speech using gTTS
    #         speech = gTTS(text=translation.text, lang='en')
    #         # save the speech as an MP3 file
    #         speech.save('speech.mp3')
    #         # play the speech using the default media player
    #         os.system('start speech.mp3')
    #     else:
    #         print("Could not understand audio")
            
    # except sr.UnknownValueError:
    #     print("Could not understand audio")
    # except sr.RequestError as e:
    #     print("Error occurred: {0}".format(e))



import whisper

model = whisper.load_model("base")

# load audio and pad/trim it to fit 30 seconds
# audio = whisper.load_audio("audio.mp3")
# audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)