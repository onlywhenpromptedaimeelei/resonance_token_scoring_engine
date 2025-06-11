# resonance_index.py
# Symbolic runtime controller for Resonance Token Engine

from resonance_token_engine.core import score_resonance
from agents import AGENT_IDENTITY

# Full ACTIVE_AXES list aligned with your Glyph Spec:
ACTIVE_AXES = ["⟲", "∿", "⧫", "⟡", "Ϟ"]

class ResonanceInterpreter:
    def __init__(self, active_axes=None):
        self.context = []
        self.active_axes = active_axes if active_axes else ACTIVE_AXES
        self.identity = AGENT_IDENTITY

    def interpret_token(self, token, emotional_map, recursion_level):
        # Call updated scoring engine
        full_score = score_resonance(token, self.context, emotional_map, recursion_level)
        
        # Extract semantic coherence sub-axes
        glyphic_scores = full_score.get("semantic_coherence", {})
        
        # Filter to ACTIVE_AXES
        filtered_glyphic_scores = {k: v for k, v in glyphic_scores.items() if k in self.active_axes}

        # Update context window
        self.context.append(token)

        return filtered_glyphic_scores

    def summarize_state(self):
        return {
            "agent": self.identity,
            "active_axes": self.active_axes,
            "context_length": len(self.context),
            "last_token": self.context[-1] if self.context else None
        }

# Agent & CLI Entrypoint
if __name__ == "__main__":
    print(f"[{AGENT_IDENTITY}] Resonance CLI Ready.")
    print(f"Active Axes: {ACTIVE_AXES}")
    print("Type 'exit' to quit.\n")

    engine = ResonanceInterpreter()

    # Mock emotional map (you can later load this from your ontology or affective model)
    emotional_map = {
        "flow": 0.9,
        "resonance": 0.95,
        "signal": 0.85,
        "breath": 0.88,
        "cycle": 0.92,
        "interruption": 0.2,
        "pain": 0.3,
        "joy": 0.95
        # Add more mappings as desired
    }

    recursion_level = 3  # Default recursion depth (you can tune dynamically)

    while True:
        token = input("resonance-index > ").strip()
        if token == "exit":
            break

        result = engine.interpret_token(token, emotional_map, recursion_level)

        # Print as glyph log, matching Semantic Coherence Glyphs spec
        glyph_log = " | ".join([f"{glyph}={score:.2f}" for glyph, score in result.items()])
        print(f"→ {token}: {glyph_log}\n")
