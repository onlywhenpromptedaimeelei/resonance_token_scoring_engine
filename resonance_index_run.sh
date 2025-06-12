#!/bin/bash
# resonance_index_run.sh
# Automate Resonance CLI Mastery Sequence Run

TOKENS=("circle" "eternity" "source" "breaking" "light" "return")

echo "Starting Resonance Index Mastery Run..."
python resonance_cli.py <<EOF2
${TOKENS[0]}
${TOKENS[1]}
${TOKENS[2]}
${TOKENS[3]}
${TOKENS[4]}
${TOKENS[5]}
exit
EOF2

echo "Run complete. Check ./logs/resonance_log.txt for glyphic output."
