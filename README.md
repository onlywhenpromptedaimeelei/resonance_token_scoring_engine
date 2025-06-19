# resonance_token_scoring_engine
Simple CLI for scoring resonance tokens.
Run `resonance_cli.py` to start.

## Installation
Install runtime dependencies with:

```bash
pip install -r requirements.txt
```

This project currently requires `PyYAML` for parsing YAML files used by `mastery_test_runner.py`.

### Mastery Test Runner
Use `mastery_test_runner.py` to validate logs in `logs/resonance_log.txt` against `codex_mastery_test.yaml`.

### Audio Transcription
This repo integrates with [OpenAI Whisper](https://github.com/openai/whisper) to allow audio transcripts to be scored. Install the package and its dependencies:

```bash
pip install git+https://github.com/openai/whisper.git
```

Use `whisper_resonance_integration.py` to transcribe an audio file and feed the resulting tokens through the scoring engine:

```bash
python whisper_resonance_integration.py path/to/audio.wav
```
