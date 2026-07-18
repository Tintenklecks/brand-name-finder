from __future__ import annotations

import random
from collections.abc import Iterable

ONSETS = ("m", "n", "l", "r", "s", "v", "f", "h", "b", "d", "k", "p")
NUCLEI = ("a", "e", "i", "o", "u", "ai", "ia", "io")
CODAS = ("", "n", "l", "r", "m", "s")
FORBIDDEN = ("q", "x", "tsch", "sch", "ght", "zz", "kk", "yy")


def _syllable(rng: random.Random, final: bool) -> str:
    onset = rng.choice(ONSETS)
    nucleus = rng.choice(NUCLEI)
    coda = rng.choice(CODAS if final else ("", "n", "l", "r"))
    return f"{onset}{nucleus}{coda}"


def is_valid(name: str, min_length: int = 4, max_length: int = 8) -> bool:
    lowered = name.lower()
    return (
        min_length <= len(lowered) <= max_length
        and lowered.isalpha()
        and not any(fragment in lowered for fragment in FORBIDDEN)
        and not any(lowered.count(vowel) > 3 for vowel in "aeiou")
    )


def generate_names(
    count: int,
    *,
    seed: int = 42,
    syllable_counts: Iterable[int] = (2, 3),
) -> list[str]:
    if count < 1:
        raise ValueError("count must be positive")

    rng = random.Random(seed)
    candidates: set[str] = set()
    attempts = 0
    max_attempts = count * 100
    options = tuple(syllable_counts)

    while len(candidates) < count and attempts < max_attempts:
        attempts += 1
        syllables = rng.choice(options)
        raw = "".join(_syllable(rng, index == syllables - 1) for index in range(syllables))
        if is_valid(raw):
            candidates.add(raw.capitalize())

    if len(candidates) < count:
        raise RuntimeError(f"generated only {len(candidates)} unique valid names")

    return sorted(candidates)
