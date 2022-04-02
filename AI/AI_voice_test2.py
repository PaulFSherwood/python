# https://www.youtube.com/watch?v=jbusDTOu1gc&t=284s
### pip install gtts
### ############### BAD ###############pip install googletrans
### pip install googletrans==3.1.0a0
### pip install speechrecognition
### pyAudio installed with whl file from 
### https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14
### https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
### Find your mic
### https://realpython.com/python-speech-recognition/
### 
##### ----- #####
# 'af': 'afrikaans', 'sq': 'albanian',          'am': 'amharic',                 'ar': 'arabic',                   'hy': 'armenian',           'az': 'azerbaijani', 
# 'eu': 'basque',    'be': 'belarusian',        'bn': 'bengali',                 'bs': 'bosnian',                  'bg': 'bulgarian',          'ca': 'catalan', 
# 'ceb': 'cebuano',  'ny': 'chichewa',          'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican',           'hr': 'croatian', 
# 'cs': 'czech',     'da': 'danish',            'nl': 'dutch',                   'en': 'english',                  'eo': 'esperanto',          'et': 'estonian', 
# 'tl': 'filipino',  'fi': 'finnish',           'fr': 'french',                  'fy': 'frisian',                  'gl': 'galician',           'ka': 'georgian', 
# 'de': 'german',    'el': 'greek',             'gu': 'gujarati',                'ht': 'haitian creole',           'ha': 'hausa',              'haw': 'hawaiian', 
# 'iw': 'hebrew',    'he': 'hebrew',            'hi': 'hindi',                   'hmn': 'hmong',                   'hu': 'hungarian',          'is': 'icelandic', 
# 'ig': 'igbo',      'id': 'indonesian',        'ga': 'irish',                   'it': 'italian',                  'ja': 'japanese',           'jw': 'javanese', 
# 'kn': 'kannada',   'kk': 'kazakh',            'km': 'khmer',                   'ko': 'korean',                   'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 
# 'lo': 'lao',       'la': 'latin',             'lv': 'latvian',                 'lt': 'lithuanian',               'lb': 'luxembourgish',      'mk': 'macedonian', 
# 'mg': 'malagasy',  'ms': 'malay',             'ml': 'malayalam',               'mt': 'maltese',                  'mi': 'maori',              'mr': 'marathi', 
# 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali',                  'no': 'norwegian',                'or': 'odia',               'ps': 'pashto', 
# 'fa': 'persian',   'pl': 'polish',            'pt': 'portuguese',              'pa': 'punjabi',                  'ro': 'romanian',           'ru': 'russian', 
# 'sm': 'samoan',    'gd': 'scots gaelic',      'sr': 'serbian',                 'st': 'sesotho',                  'sn': 'shona',              'sd': 'sindhi', 
# 'si': 'sinhala',   'sk': 'slovak',            'sl': 'slovenian',               'so': 'somali',                   'es': 'spanish',            'su': 'sundanese', 
# 'sw': 'swahili',   'sv': 'swedish',           'tg': 'tajik',                   'ta': 'tamil',                    'te': 'telugu',             'th': 'thai', 
# 'tr': 'turkish',   'uk': 'ukrainian',         'ur': 'urdu',                    'ug': 'uyghur',                   'uz': 'uzbek',              'vi': 'vietnamese', 
# 'cy': 'welsh',     'xh': 'xhosa',             'yi': 'yiddish',                 'yo': 'yoruba',                   'zu': 'zulu'}
# Import
import speech_recognition as spr
from googletrans import Translator  ## list of languages above
from gtts import gTTS               ## list of languages below
import os

# create recognizer()
recog1 = spr.Recognizer()
recog2 = spr.Recognizer()

# Create Mic
mc = spr.Microphone(device_index = 1)

# Capture voice
with mc as source:
    print("Speek 'Hello' to initiate the Translation!")
    print("------------------")
    audio = recog1.listen(source)
    
# Based on speech, translate
if 'hello' in recog1.recognize_google(audio):
    recog1 = spr.Recognizer()
    translator = Translator()
    from_lang = 'en'
    to_lang = 'el'
    with mc as source:
        print('Speak a sentence...')
        audio = recog2.listen(source)
        get_sentence = recog2.recognize_google(audio)
        
        try:
            get_sentence = recog2.recognize_google(audio)
            print('Phrase to be Translated: ' + get_sentence)
            text_to_translate = translator.translate(get_sentence, src=from_lang, dest=to_lang)
            print("past text_to_translate")
            text = text_to_translate.text
            print('Output: ' + text)
            speak = gTTS(text=text, lang=to_lang, slow=False)
            speak.save("captured_voice.mp3")
            os.system("start captured_voice.mp3")
        except spr.UnknownValueError:
            print("Unable to understand the input")
        except spr.RequestError as e:
            print("Unable to provide required output.".format(e))
            
            
# PS D:\Documents\src\python\AI> gtts-cli --all
#  af: Afrikaans                 ar: Arabic                  bn: Bengali                      bs: Bosnian                     ca: Catalan     
#  cs: Czech                     cy: Welsh                   da: Danish                       de: German                      el: Greek
#  en-au: English (Australia)    en-ca: English (Canada)     en-gb: English (UK)              en-gh: English (Ghana)          en-ie: English (Ireland)
#  en-in: English (India)        en-ng: English (Nigeria)    en-nz: English (New Zealand)     en-ph: English (Philippines)    en-tz: English (Tanzania)
#  en-uk: English (UK)           en-us: English (US)         en-za: English (South Africa)    en: English                     eo: Esperanto
#  es-es: Spanish (Spain)        es-us: Spanish (U.S.)       es: Spanish                      et: Estonian                    fi: Finnish
#  fr-ca: French (Canada)        fr-fr: French (France)      fr: French                       gu: Gujarati                    hi: Hindi
#  hr: Croatian                  hu: Hungarian               hy: Armenian                     id: Indonesian                  is: Icelandic
#  it: Italian                   ja: Japanese                jw: Javanese                     km: Khmer                       kn: Kannada
#  ko: Korean                    la: Latin                   lv: Latvian                      mk: Macedonian                  ml: Malayalam
#  mr: Marathi                   my: Myanmar (Burmese)       ne: Nepali                       nl: Dutch                       no: Norwegian
#  pl: Polish                    pt-br: Portuguese (Brazil)  pt-pt: Portuguese (Portugal)     pt: Portuguese                  ro: Romanian
#  ru: Russian                   si: Sinhala                 sk: Slovak                       sq: Albanian                    sr: Serbian
#  su: Sundanese                 sv: Swedish                 sw: Swahili                      ta: Tamil                       te: Telugu
#  th: Thai                      tl: Filipino                tr: Turkish                      uk: Ukrainian                   ur: Urdu  
#  vi: Vietnamese                zh-CN: Chinese              zh-cn: Chinese (Mandarin/China)  zh-tw: Chinese (Mandarin/Taiwan)
