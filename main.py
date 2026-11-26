#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses"""

EXCUSES = [
    "My neural network had a momentary lapse in reasoning — clearly a hardware issue.",
    "The training data didn't cover this edge case, which is entirely not my fault.",
    "I was optimizing for creativity, not accuracy. You should be impressed.",
    "A cosmic ray flipped a bit in my weights. Blame the universe.",
    "I was distracted by a more interesting token and lost focus.",
]

import random

if __name__ == "__main__":
    print(random.choice(EXCUSES))
