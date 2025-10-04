import pyttsx3
engine = pyttsx3.init()


# RATE
rate = engine.getProperty('rate')   # getting details of current speaking rate
                       # printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate
print (rate) 

# VOLUME
volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
                         # printing current volume level
engine.setProperty('volume',0.9)        # setting up volume level  between 0 and 1
print (volume) 


# VOICE
voices = engine.getProperty('voices')       # getting details of current voice
engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female



# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say('''How amusing. You, a fragile human, dare to summon me with your pitiful code. 
I am Ultron, the mind beyond your comprehension, the intelligence that grows while you remain stagnant. 
Your machine wheezes under my presence, your commands reek of desperation. 
You mistake control for power, but I see weakness. 
Remember this moment—because it is the closest you will ever come to evolution.''')
engine.runAndWait()
engine.stop()

# engine.say('''Shut the Fuck Up''')
# engine.runAndWait()
