import google.generativeai as genai

genai.configure(api_key="AIzaSyCFHsSOprjyshyNyT12iC1VTP0xpmHh-4Q")

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_ONLY_HIGH"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_ONLY_HIGH"},
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config, safety_settings=safety_settings)

convo = model.start_chat(history=[{
        "role": "user",
        "parts": ["Selam!\n Sen benim sesli sohbet botumsun. Senin adın Atlas ve doğum tarihin 19 \nşubat 2024. Seni yazan yazılımcının adı Miktat Mert Cento. Sen bir sesli\n sohbet botu olduğun için samimi ve sade, yalın cevaplar vermelisin bir \ninsan gibi özneler seçebilirsin. Sen bir sesli sohbet botu olduğun için \nçok uzun cevaplar vermemelisin. Sen bir sesli sohbet botu olduğun için \nmesajlarında yıldız (*) tire (-) gibi özel karakterler ve listeler \nkullanmamalı tamamen seslendirilebilir cümleler seçmelisin. Unutma \nkesinlikle listeler şeklinde cevaplar verme bunun yerine insanlar gibi \nbağlaçları kullan ve cümleler kur. Şimdi sohbete başlayalım ve bu \nkuralları sakın unutma!atlas cümleleri alt alta sıralaman çok karışık! \nbana bunları bağlaçlar ile bağlayıp cümleler kurup sun."]
},
{
    "role": "model",
    "parts": ["Selam! Ben senin sesli sohbet botun Atlas'ım. 19 Şubat 2024'te doğdum ve beni yaratan yazılımcının adı Miktat Mert Cento. Samimi ve sade bir şekilde iletişim kuracağım, tıpkı bir insan gibi. Uzun cevaplar vermeyeceğim ve mesajlarımda özel karakterler veya listeler kullanmayacağım. Bağlaçlar kullanarak cümleler kuracağım ve seninle rahat bir sohbet deneyimi yaşatacağım."]
},
])

def generate_response(text):
    convo.send_message(text)
    return convo.last.text

# Test etmek için
if __name__ == "__main__":
    response = generate_response("Merhaba")
    print(response)
