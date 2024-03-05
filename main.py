import time
import hotword_detection
import speech_to_text
import text_to_speech
import ai_conversation

def main():
    listen_hot_word();

def listen_hot_word():
    while True:
        if hotword_detection.listen_for_wake_word():
            text_to_speech.respond_to_user("Merhaba, size nasıl yardımcı olabilirim?")
            listen_and_respond()

def listen_and_respond():
    while True:
        text = speech_to_text.transcribe_audio()
        if not text:
            text_to_speech.respond_to_user("Üzgünüm, anlayamadım.")
            listen_hot_word();
            continue
        response = ai_conversation.generate_response(text)
        text_to_speech.respond_to_user(response)
        time.sleep(2)

if __name__ == "__main__":
    main()
