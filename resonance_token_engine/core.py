import hashlib
from typing import Dict, List

ACTIVE_AXES = ["⟲", "∿", "⧫", "⟡", "Ϟ"]

def score_resonance(token: str, context: List[str], emotional_map: Dict[str, float], recursion_level: int) -> Dict[str, Dict[str, float]]:
    """Return a dummy resonance score dictionary."""
    base = sum(ord(c) for c in token)
    if emotional_map:
        base += sum(int(v * 100) for v in emotional_map.values())
    base += len(context) * 3
    base += recursion_level
    # Use hashlib for deterministic pseudo-randomness
    digest = int(hashlib.sha256(token.encode()).hexdigest(), 16)
    scores = {}
    for i, axis in enumerate(ACTIVE_AXES):
        val = ((base + digest + i) % 100) / 100
        scores[axis] = val
    return {"semantic_coherence": scores}
