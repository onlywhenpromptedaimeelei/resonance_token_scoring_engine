# resonance_token_scoring_engine

Simple CLI for scoring resonance tokens.

## Setup
Install dependencies first:
```bash
pip install -r requirements.txt
```

## Running the CLI
Accept the license and start the interactive prompt:
```bash
RES_LICENSE_ACCEPTED=true python resonance_cli.py
```

## Mastery Test Runner
After collecting logs with the CLI, validate them against `codex_mastery_test.yaml`:
```bash
python mastery_test_runner.py
```
Logs are read from `logs/resonance_log.txt`.
