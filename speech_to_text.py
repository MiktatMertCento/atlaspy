import speech_recognition as sr

def transcribe_audio():
    r = sr.Recognizer()
    print("Listening...")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='tr-TR')
            print(f"Siz söylediniz: {text}")
            return text
        except sr.UnknownValueError:
            return None

# Test etmek için
if __name__ == "__main__":
    transcribe_audio()
