import os
import requests
from dotenv import load_dotenv

load_dotenv()
resp = requests.post(
    "https://api.deepgram.com/v1/speak",
    params={"model": "aura-2-thalia-en"},
    headers={
        "Authorization": f"Token {os.getenv('DEEPGRAM_API_KEY')}",
        "Content-Type": "application/json",
    },
    json={"text": "The audit is complete. Cloud costs are down."},
    timeout=60,
)
resp.raise_for_status()

with open("bmax_voice_memo.mp3", "wb") as f:
    f.write(resp.content)
print("Wrote bmax_voice_memo.mp3")