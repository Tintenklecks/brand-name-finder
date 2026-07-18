from __future__ import annotations

from .models import NameCandidate

SOFT_CONSONANTS = set("lmnrsvfh")
OPEN_ENDINGS = ("a", "e", "i", "o", "u")
COMMON_STARTUP_SUFFIXES = ("io", "ly", "ora", "ivo")


def _clamp(value: float) -> float:
    return max(0.0, min(100.0, value))


def score_name(name: str, profile: str = "warm") -> NameCandidate:
    lowered = name.lower()
    length = len(lowered)
    vowels = sum(character in "aeiou" for character in lowered)
    soft = sum(character in SOFT_CONSONANTS for character in lowered)

    pronunciation = 100 - abs(length - 6) * 8
    pronunciation -= (
        12
        if any(a == b for a, b in zip(lowered, lowered[1:], strict=False))
        else 0
    )

    memorability = 92 - abs(length - 5) * 7
    memorability += 5 if lowered[0] != lowered[-1] else -4

    warmth = 55 + soft * 6 + vowels * 4
    warmth += 8 if lowered.endswith(OPEN_ENDINGS) else 0

    distinctiveness = 88
    distinctiveness -= 18 if lowered.endswith(COMMON_STARTUP_SUFFIXES) else 0
    distinctiveness -= 8 if length <= 4 else 0

    spelling_clarity = 96
    spelling_clarity -= 15 if "i" in lowered and "y" in lowered else 0
    spelling_clarity -= 10 if any(cluster in lowered for cluster in ("ai", "ia", "io")) else 0

    return NameCandidate(
        name=name,
        profile=profile,
        pronunciation=_clamp(pronunciation),
        memorability=_clamp(memorability),
        warmth=_clamp(warmth),
        distinctiveness=_clamp(distinctiveness),
        spelling_clarity=_clamp(spelling_clarity),
    )


def rank_names(names: list[str], profile: str = "warm") -> list[NameCandidate]:
    return sorted(
        (score_name(name, profile=profile) for name in names),
        key=lambda candidate: (-candidate.score, candidate.name),
    )
