import pyttsx3
import speech_recognition as sr
import openai
import env

# openai key
openai.api_key = env.OPEN_AI_KEY

# initailize speech engine
engine = pyttsx3.init()

def speak(word):
    engine.setProperty('rate', 135)
    engine.setProperty('volume', 0.8)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say(str(word))
    engine.runAndWait()
    engine.stop()

# initalize speech Recognizer
rec = sr.Recognizer()
speak('hello sir, i am waiting for your command')
with sr.Microphone() as source:
    audio = rec.listen(source)
    speak('i am computing a result for your request please wait i will be done very soon ')

text = rec.recognize_google(audio)

discussion = openai.Completion.create(
    model="text-davinci-002",
    prompt=text,
    max_tokens=100,
)

answer = discussion
print(answer)



