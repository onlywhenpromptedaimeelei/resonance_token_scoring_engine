import pytest

from resonance_token_engine.core import (
    compute_phase_alignment,
    compute_symbolic_echo,
    compute_referential_density,
    compute_contextual_continuity,
    compute_affective_compatibility,
    measure_affective_pulse,
    normalize_recursion,
    rhythmic_alignment,
    compute_density,
    score_resonance,
)


def test_compute_phase_alignment():
    context = ["aa", "bbb", "cc", "d", "eeee"]
    assert compute_phase_alignment("test", context) == 3 / 5


def test_compute_symbolic_echo():
    context = ["wave", "signal", "noise"]
    assert compute_symbolic_echo("wave", context) == 1 / 2
    assert compute_symbolic_echo("noise", context) == 0


def test_compute_referential_density():
    context = ["a"] * 10
    assert compute_referential_density("resonance", context) == (2 + 2) / 10


def test_compute_contextual_continuity():
    assert compute_contextual_continuity("flow", ["something"]) == 1
    assert compute_contextual_continuity("x", ["a"]) == 0
    assert compute_contextual_continuity("x", []) == 0.5


def test_compute_affective_compatibility():
    m = {"happy": 0.9}
    assert compute_affective_compatibility("happy", m) == 0.9
    assert compute_affective_compatibility("sad", m) == 0.5


def test_measure_affective_pulse():
    m = {"happy": 0.9}
    assert measure_affective_pulse("happy", m) == 0.9
    assert measure_affective_pulse("meh", m) == 0.5


def test_normalize_recursion():
    assert normalize_recursion(5) == 0.5
    assert normalize_recursion(15) == 1.0


def test_rhythmic_alignment():
    assert rhythmic_alignment("even", []) == 1.0
    assert rhythmic_alignment("odd", []) == 0.75


def test_compute_density():
    assert compute_density(list(range(10))) == 0.5
    assert compute_density(list(range(25))) == 1.0


def test_score_resonance():
    token = "wave"
    context = ["signal", "flow", "pulse"]
    emap = {"wave": 0.8}
    result = score_resonance(token, context, emap, 3)
    assert result["emotional_charge"] == 0.8
    assert result["recursion_depth"] == 0.3
    assert 0 <= result["field_saturation"] <= 1
    sc = result["semantic_coherence"]
    assert set(sc.keys()) == {"\u27F2", "\u223F", "\u29EB", "\u27E1", "\u03DE"}
