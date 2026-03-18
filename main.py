import speech_recognition as sr
import whisper
import openai
from gtts import gTTS
import os
from playsound import playsound

openai.api_key = "SUA_API_KEY"

recognizer = sr.Recognizer()
model = whisper.load_model("base")

def capturar_audio():
    with sr.Microphone() as source:
        print("Fale algo...")
        audio = recognizer.listen(source)

        with open("audio.wav", "wb") as f:
            f.write(audio.get_wav_data())

    result = model.transcribe("audio.wav")
    return result["text"]

def responder(texto):
    resposta = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": texto}]
    )
    return resposta.choices[0].message.content

def falar(texto):
    tts = gTTS(texto, lang='pt')
    tts.save("resposta.mp3")
    playsound("resposta.mp3")

while True:
    try:
        pergunta = ouvir()
        print("Você:", pergunta)

        resposta = responder(pergunta)
        print("ChatGPT:", resposta)

        falar(resposta)

    except Exception as e:
        print("Erro:", e)
