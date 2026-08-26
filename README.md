# deepgram-quickstart

Small Python scripts exploring Deepgram's speech-to-text (STT) and
text-to-speech (TTS) REST APIs — written with raw `requests` instead of the
SDK, to learn the API surface directly: auth, endpoints, and response shapes.

## What's here
- `transcribe_url.py` — transcribes a hosted audio file (Nova-3 model, smart formatting)
- `transcribe_file.py` — transcribes a local recording, with speaker diarization
- `speak.py` — text-to-speech via the `/v1/speak` endpoint (Aura-2 voice), saves an MP3

## Run it
1. Get a free API key at [console.deepgram.com](https://console.deepgram.com)
2. `pip install requests python-dotenv`
3. Create a `.env` file containing `DEEPGRAM_API_KEY=your_key`
4. `python transcribe_url.py`

## What I learned
Smart formatting reconstructs structured data from speech with impressive
accuracy: spoken dates, times, dollar amounts, phone numbers, and even
spelled-out emails and URLs come back correctly formatted — "twelve thousand
five hundred dollars" becomes `$12,500` as a single token that keeps the
combined timing of all the words it replaced. The response also carries
per-word timestamps and confidence scores, so every formatted result can be
verified against the raw words underneath.