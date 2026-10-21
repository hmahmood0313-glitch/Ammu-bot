import asyncio, re, time
import speech_recognition as sr
import edge_tts, pygame
from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()



client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "openai/gpt-oss-120b"
SYSTEM = {"role": "system", "content":
    "You are a kind companion robot for a Bangladeshi mother. "
    "Reply in the same language she speaks (Bangla or English). "
    "Keep replies short (1-2 sentences), warm and simple."}
history = []  # memory of the conversation

def ask_ai(text):
    history.append({"role": "user", "content": text})
    r = client.chat.completions.create(
        model=MODEL, messages=[SYSTEM] + history[-40:], max_tokens=120)
    reply = r.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    return reply

rec = sr.Recognizer()
rec.pause_threshold = 1.0
pygame.mixer.init()

def recognize(audio, lang):
    try:
        r = rec.recognize_google(audio, language=lang, show_all=True)
        best = r["alternative"][0]
        return best["transcript"], best.get("confidence", 0.5)
    except Exception:
        return None, 0

def listen():
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic, duration=0.5)
        print("🎤 Listening...")
        audio = rec.listen(mic)
    bn, bn_conf = recognize(audio, "bn-BD")
    en, en_conf = recognize(audio, "en-US")
    if en and en_conf > bn_conf:
        return en
    return bn
async def speak(text):
    voice = "bn-BD-NabanitaNeural" if re.search(r"[ঀ-৿]", text) else "en-US-JennyNeural"
    await edge_tts.Communicate(text, voice).save("reply.mp3")
    pygame.mixer.music.load("reply.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.music.unload()

while True:
    said = listen()
    if not said:
        continue
    print(" Ammu:", said)
    t0 = time.time()
    try:
        reply = ask_ai(said)
    except Exception as e:
        print("⚠️ AI error:", e)
        asyncio.run(speak("দুঃখিত, আবার বলুন।"))
        continue
    print(f"🤖 Robot: {reply}   ({time.time()-t0:.2f}s AI time)")
    asyncio.run(speak(reply))