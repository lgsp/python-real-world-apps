from gtts import gTTS
# python3.8 -m pip install gtts
from playsound import playsound
# python3.8 -m pip install playsound



def write_your_speech(audio_name, language, instructions, listen):
    speech = gTTS(text = instructions, lang = language, slow=False)
    speech.save(audio_name)
    print(listen.upper())
    playsound(audio_name)
    
    your_speech = input(instructions + "\n")
    if language == 'en':
        your_audio = 'your_speech.mp3'
    elif language == 'fr':
        your_audio = 'votre_discours.mp3'
    elif language == 'ru':
        your_audio = 'your_russian.mp3'
        
    your_speech = gTTS(text = your_speech, lang = language, slow=False)

    your_speech.save(your_audio)
    print(listen.upper())
    playsound(your_audio)


    
audio_intro_en = 'intro_en.mp3'
en = 'en'
text_en = """
What language are you the most comfortable with?
For English type 'E'.
For French type 'F'.
For Russian type 'R'.
"""
intro_en = gTTS(text = text_en, lang = en, slow=False)


intro_en.save(audio_intro_en)
playsound(audio_intro_en)


english = input(text_en)

if english.upper() == 'E':
    audio_name = 'speech.mp3'
    language = 'en'
    instructions = "Enter your text which you want to convert into audio file:"
    listen = "Listen to the speaker and execute instructions"

elif english.upper() == 'F':
    audio_name = 'discours.mp3'
    language = 'fr'
    instructions = "Entrer votre texte que vous voulez convertir en fichier audio :"
    listen = "Ecoutez la voix off et exécutez les instructions"

elif english.upper() == 'R':
    audio_name = 'russian.mp3'
    language = 'ru'
    instructions = "Введите текст, который вы хотите преобразовать в аудиофайл:"
    listen = "Прослушайте голос за кадром и выполните инструкции"

write_your_speech(audio_name, language, instructions, listen)

