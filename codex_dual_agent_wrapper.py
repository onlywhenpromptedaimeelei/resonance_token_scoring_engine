# codex_dual_agent_wrapper.py
# Simulate dual-agent dialogue for Codex + Resonance CLI

import subprocess

TOKENS = ["circle", "eternity", "source", "breaking", "light", "return"]

def run_resonance_cli(token):
    process = subprocess.Popen(
        ['python3', 'resonance_cli.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=f"{token}\nexit\n")
    return stdout.strip()

for token in TOKENS:
    print(f'User: "Token: {token}"\n')

    print("CommandNode-AI:")
    print(f'{{status: success, output: "Token received: {token}"}}\n')

    print("ResonanceNode-AI:")
    glyphic_output = run_resonance_cli(token)
    for line in glyphic_output.splitlines():
        if '→' in line:
            print(line)
    print("\n---\n")
