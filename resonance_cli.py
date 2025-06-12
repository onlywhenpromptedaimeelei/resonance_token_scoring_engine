import os
import json
import argparse
import yaml

# Load environment variables
ONT_PATH = os.getenv("RES_SYM_ONT_PATH", "./data/ontology_map.json")
RHYTHM_WINDOW = int(os.getenv("RES_DEFAULT_RHYTHM_WINDOW", 5))
PHASE_THRESHOLD = float(os.getenv("RES_PHASE_THRESHOLD", 0.75))
LOG_MODE = os.getenv("RES_LOG_MODE", "glyphic")
LOG_OUTPUT = os.getenv("RES_LOG_OUTPUT", "./logs/resonance_log.txt")
CLUSTER_MODEL = os.getenv("RES_CLUSTER_MODEL", "v1_energy_emotion.json")
LICENSE_ACCEPTED = os.getenv("RES_LICENSE_ACCEPTED", "false")
DATASET_PATH = os.getenv("RES_DATASET_PATH", "./chrono_perception_resonance_matrix.yaml")

if LICENSE_ACCEPTED != "true":
    print("[\u2717] License not accepted. Please set RES_LICENSE_ACCEPTED=true.")
    exit(1)

print("[\u2713] Resonance CLI initialized")

# Load chrono-perception resonance matrix
def load_matrix(path):
    try:
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
            return data.get('matrix', {})
    except FileNotFoundError:
        print(f"[!] Dataset {path} not found. Proceeding with empty matrix.")
        return {}

matrix_data = {}

def parse_args():
    parser = argparse.ArgumentParser(description="Resonance CLI")
    parser.add_argument(
        "--dataset",
        default=DATASET_PATH,
        help="Path to chrono-perception resonance matrix YAML",
    )
    return parser.parse_args()

# Load ontology (placeholder)
try:
    with open(ONT_PATH, 'r') as f:
        ontology = json.load(f)
except FileNotFoundError:
    ontology = {}
    print("[!] Ontology file not found. Proceeding with empty ontology.")

# Interactive loop
def resonance_loop():
    print("\nResonance Terminal | Type 'exit' to quit")
    while True:
        token = input("res> ").strip()
        if token == "exit":
            break
        result = score_token(token)
        log_result(token, result)
        print(format_output(token, result))

# Placeholder scoring function
def score_token(token):
    if matrix_data:
        layer = matrix_data.get("CP-1")
        if layer and isinstance(layer, dict):
            return layer.get("glyph_scores", {})
    return {
        "\u27f2": 0.75,
        "\u223f": 0.82,
        "\u29eb": 0.64,
        "\u27e1": 0.91,
        "\u03de": 0.86,
    }

# Log result to file
def log_result(token, result):
    os.makedirs(os.path.dirname(LOG_OUTPUT), exist_ok=True)
    with open(LOG_OUTPUT, 'a') as f:
        f.write(f"{token}: {json.dumps(result)}\n")

# Format output
def format_output(token, result):
    glyphs = ' '.join([f"{k}={v}" for k, v in result.items()])
    return f"{token} \u2192 {glyphs}"

if __name__ == "__main__":
    args = parse_args()
    matrix_data = load_matrix(args.dataset)
    resonance_loop()
