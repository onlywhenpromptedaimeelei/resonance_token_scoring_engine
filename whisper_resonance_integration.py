import sys
from whisper_transcriber import transcribe_audio
from resonance_cli import score_token, log_result, format_output


def transcribe_and_score(audio_path):
    text = transcribe_audio(audio_path)
    if not text:
        print("No text transcribed from audio.")
        return
    for token in text.split():
        res = score_token(token)
        log_result(token, res)
        print(format_output(token, res))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python whisper_resonance_integration.py <audio_file>")
        sys.exit(1)
    transcribe_and_score(sys.argv[1])
