#!/usr/bin/env python3
# Licensed under the Apache License 2.0
# mastery_test_runner.py
# Auto-validate Resonance Token Mastery Sequence against codex_mastery_test.yaml

import yaml
import re

LOG_PATH = './logs/resonance_log.txt'
TEST_YAML_PATH = './codex_mastery_test.yaml'

# Load mastery test spec
with open(TEST_YAML_PATH, 'r') as f:
    test_spec = yaml.safe_load(f)

# Parse log
glyph_pattern = re.compile(r'→ (\w+): ⟲=(\d+\.\d+) \| ∿=(\d+\.\d+) \| ⧫=(\d+\.\d+) \| ⟡=(\d+\.\d+) \| Ϟ=(\d+\.\d+)')
tokens = []
glyphics = []

with open(LOG_PATH, 'r') as f:
    for line in f:
        match = glyph_pattern.search(line)
        if match:
            token, circ, echo, dens, cont, affect = match.groups()
            tokens.append(token)
            glyphics.append((float(circ), float(echo), float(dens), float(cont), float(affect)))

# Validate ⟲
phase_pass = all(circ >= test_spec['expected_trends']['⟲']['min'] for circ, *_ in glyphics)

# Validate ∿ trend increasing over required tokens
def is_increasing(values):
    return all(x < y for x, y in zip(values, values[1:]))

echo_indices = [i-1 for i in test_spec['expected_trends']['∿']['points']]  # 0-based
echo_values = [glyphics[i][1] for i in echo_indices]
echo_pass = is_increasing(echo_values)

# Validate ⟡ collapse and recovery
collapse_index = test_spec['expected_trends']['⟡']['collapse_at'] - 1
collapse_value = glyphics[collapse_index][3]
collapse_pass = collapse_value <= 0.50

recovery_indices = [i-1 for i in test_spec['expected_trends']['⟡']['recovery_points']]
recovery_values = [glyphics[i][3] for i in recovery_indices]
recovery_pass = all(val >= test_spec['expected_trends']['⟡']['recovery_min'] for val in recovery_values)

# Report
print("\n===== MASTER TEST RESULTS =====\n")
print(f"⟲ Phase Alignment ≥ {test_spec['expected_trends']['⟲']['min']} → {'PASS' if phase_pass else 'FAIL'}")
print(f"∿ Symbolic Echo Increasing → {'PASS' if echo_pass else 'FAIL'}")
print(f"⟡ Collapse at token {test_spec['expected_trends']['⟡']['collapse_at']} → {'PASS' if collapse_pass else 'FAIL'}")
print(f"⟡ Recovery at tokens {test_spec['expected_trends']['⟡']['recovery_points']} → {'PASS' if recovery_pass else 'FAIL'}")

if phase_pass and echo_pass and collapse_pass and recovery_pass:
    print("\n🎖️ MASTER TEST PASSED! 🎖️\n")
else:
    print("\n❌ MASTER TEST FAILED ❌\n")
