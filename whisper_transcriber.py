import sys

try:
    import whisper
except ImportError as e:
    raise SystemExit("whisper package not installed. Install with 'pip install git+https://github.com/openai/whisper.git'")

def transcribe_audio(audio_path, model_name="base"):
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path)
    return result.get("text", "")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python whisper_transcriber.py <audio_file>")
        sys.exit(1)
    text = transcribe_audio(sys.argv[1])
    print(text)
