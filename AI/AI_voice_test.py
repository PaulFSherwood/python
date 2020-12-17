apikey = 'QcwBt61slEzpejBNYKSVddfJytHFETHJlQzel_E9hmpF'
url = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/d386fcaa-29a0-47a0-981b-8e8f5fcd55c1'

# import dependencies
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Setup service
authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
lt.set_service_url(url)

translation = lt.translate(text='In the beginning God created the heaven and the earth..', model_id='en-de').get_result()

translation

translation['translations'][0]['translation']

ttsapikey = '3WuVp1YBwb069ZBD8nfyCjxpMR6bwsu7Sfmhx2lXsEVU'
ttsurl = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/4a4be4a1-81c5-4092-8755-a262566aca48'

from ibm_watson import TextToSpeechV1

#authenticate
ttsauthenticator = IAMAuthenticator(ttsapikey)
tts = TextToSpeechV1(authenticator=ttsauthenticator)
tts.set_service_url(ttsurl)

translation = lt.translate(text='In the beginning God created the heaven and the earth.', model_id='en-de').get_result()

text = translation['translations'][0]['translation']
text

with open('./help.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='ar-MS_OmarVoice').get_result()
    audio_file.write(res.content)

