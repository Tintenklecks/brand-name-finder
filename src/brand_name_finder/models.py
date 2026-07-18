from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class NameCandidate:
    name: str
    profile: str
    pronunciation: float
    memorability: float
    warmth: float
    distinctiveness: float
    spelling_clarity: float

    @property
    def score(self) -> float:
        weighted = (
            self.pronunciation * 0.25
            + self.memorability * 0.20
            + self.warmth * 0.15
            + self.distinctiveness * 0.20
            + self.spelling_clarity * 0.20
        )
        return round(weighted, 2)
