# resonance_token_engine/core.py

# Resonance Token Scoring Engine – Semantic Coherence Full Implementation
# Aligned with Resonance CLI Spec v0.1 + Semantic Coherence Glyphs-1.pdf


def score_resonance(token, context, emotional_map, recursion_level):
    """
    Returns a resonance vector for a token based on the Lei Field Model.

    Inputs:
        token: str – the word or phrase to score
        context: list[str] – surrounding tokens for coherence mapping
        emotional_map: dict – semantic-affective graph for charge estimation
        recursion_level: int – depth of semantic layering this token exists within

    Returns:
        dict – resonance vector with named axes
    """
    return {
        "semantic_coherence": {
            "⟲": compute_phase_alignment(token, context),
            "∿": compute_symbolic_echo(token, context),
            "⧫": compute_referential_density(token, context),
            "⟡": compute_contextual_continuity(token, context),
            "Ϟ": compute_affective_compatibility(token, emotional_map)
        },
        "emotional_charge": measure_affective_pulse(token, emotional_map),
        "recursion_depth": normalize_recursion(recursion_level),
        "temporal_harmony": rhythmic_alignment(token, context),
        "field_saturation": compute_density(context)
    }

# ——————————————————
# Sub-Axis Implementations
# ——————————————————


def compute_phase_alignment(token, context):
    # Rhythm fit: length even vs odd → simple rhythm heuristic
    downstream_in_phase = sum(len(t) % 2 == 0 for t in context[-5:])  # last 5 tokens
    P = downstream_in_phase / 5.0
    if P > 1.0:
        P = 1.0
    return P


def compute_symbolic_echo(token, context):
    # Simple symbolic cluster heuristic (placeholder)
    ENERGY_FIELD = {"signal", "wave", "pulse", "cycle", "frequency", "flow"}
    context_clusters = sum(1 for t in context if t in ENERGY_FIELD)
    token_in_cluster = token in ENERGY_FIELD
    shared_clusters = 1 if token_in_cluster else 0
    total_context_clusters = max(1, context_clusters)
    echo_score = shared_clusters / total_context_clusters
    if echo_score > 1.0:
        echo_score = 1.0
    return echo_score


def compute_referential_density(token, context):
    connected_clusters = 2 if token in {"resonance", "harmony", "field", "cycle"} else 1
    recursion_depth = len(context) // 5
    max_expected_value = 10
    density_score = (connected_clusters + recursion_depth) / max_expected_value
    if density_score > 1.0:
        density_score = 1.0
    return density_score


def compute_contextual_continuity(token, context):
    continuity_thread = {"breath", "flow", "pulse", "resonance", "cycle"}
    if not context:
        return 0.5
    thread_match = token in continuity_thread
    thread_deviation = 0 if thread_match else 1
    max_allowed_deviation = 1
    continuity_score = 1 - (thread_deviation / max_allowed_deviation)
    if continuity_score < 0:
        continuity_score = 0
    return continuity_score


def compute_affective_compatibility(token, emotional_map):
    return emotional_map.get(token, 0.5)

# ——————————————————
# Supporting Axes
# ——————————————————


def measure_affective_pulse(token, emotional_map):
    return emotional_map.get(token, 0.5)


def normalize_recursion(level):
    return min(level / 10.0, 1.0)


def rhythmic_alignment(token, context):
    return 1.0 if len(token) % 2 == 0 else 0.75


def compute_density(context):
    return min(len(context) / 20.0, 1.0)
