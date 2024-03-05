from gtts import gTTS
import os

def respond_to_user(text):
    print("Cevap:", text)
    tts = gTTS(text=text, lang='tr')
    tts.save("response.mp3")
    os.system("mpg123 response.mp3")

# Test etmek için
if __name__ == "__main__":
    respond_to_user("Merhaba, size nasıl yardımcı olabilirim?")
