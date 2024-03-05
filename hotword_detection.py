import speech_recognition as sr

def listen_for_wake_word():
    r = sr.Recognizer()
    print("Listening for 'Hey Atlas'...")

    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language='tr-TR')
                if "hey atlas" in text.lower():
                    print("Wake word detected.")
                    return True
            except sr.UnknownValueError:
                pass

# Test etmek için
if __name__ == "__main__":
    listen_for_wake_word()
