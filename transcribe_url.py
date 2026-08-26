
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("DEEPGRAM_API_KEY")
if not API_KEY:
    raise RuntimeError("DEEPGRAM_API_KEY not found - is .env present?")

URL = "https://api.deepgram.com/v1/listen"
params = {"model":   "nova-3",  "smart_format":  "true"}
headers = {"Authorization": f"Token {API_KEY}", "Content-Type": "application/json", }

payload = {"url" : "https://dpgr.am/spacewalk.wav"}

resp = requests.post(URL,  params=params, headers=headers, json=payload, timeout=60)
resp.raise_for_status()                         #explodes on 4xx/5xx
data=resp.json()


alt = data["results"]["channels"][0]["alternatives"][0]
print("Transcript:", alt["transcript"])
print("Confidence:",  round(alt["confidence"], 3))
print("Audio duration (s):", data["metadata"]["duration"])

