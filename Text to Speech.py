# Import the required module for TTS conversion

from gtts import gTTS
import os

# The text you want to convert to audio
mytext = "Pizda mă-tii"

# Language
language = 'ro'

# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
file = gTTS(text = mytext, lang = language, slow = False)

# Saving the audio file
file.save("salut.mp3")
