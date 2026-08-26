import os
import requests
import  json
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("DEEPGRAM_API_KEY")
if not API_KEY:
    raise RuntimeError("DEEPGRAM_API_KEY not found - is .env present?")

URL = "https://api.deepgram.com/v1/listen"
params = {"model":   "nova-3",  "smart_format":  "true" , "diarize": "true"}
headers = {"Authorization": f"Token {API_KEY}", "Content-Type": "audio/wav", }

with open("bmax_voice_memo.wav" , "rb") as f:
    resp=requests.post(URL, params=params, headers=headers, data=f,  timeout=120)

    resp.raise_for_status()
    data = resp.json()

with open("response.json", "w") as f:
    json.dump(data, f, indent=2)

print("Saved response.json")


alt = data["results"] ["channels"][0]["alternatives"][0]
print(alt["transcript"])

