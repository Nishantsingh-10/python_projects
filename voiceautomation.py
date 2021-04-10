import speech_recognition as sr
record = sr.Recognizer()
with sr.Microphone() as source:
    print("what you want....")
    audio=record.listen(source)
    print("done.")
data = record.recognize_google(audio)
print(data)
