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

def generate_response(text):
    convo = model.start_chat(history=[{"role": "user", "parts": [text]}])
    return convo.last.text

# Test etmek için
if __name__ == "__main__":
    response = generate_response("Merhaba")
    print(response)
