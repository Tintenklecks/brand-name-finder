# Brand Name Finder

Generate, score, and pre-check brand-name candidates before manual legal review.

## Current scope

The first milestone is intentionally local and deterministic:

- generate pronounceable artificial names from configurable phonetic building blocks
- reject obviously awkward letter combinations
- score pronunciation, memorability, warmth, distinctiveness, and spelling clarity
- export the highest-ranked candidates to CSV
- reproduce every run through a fixed random seed

External providers for App Store, RDAP/domain, GitHub, web search, and trademark checks will be added as separate adapters. Their results are pre-screening signals, never legal clearance.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
```

## Generate candidates

```bash
brand-name-finder generate --count 5000 --top 40 --seed 42 --output candidates.csv
```

## Run tests

```bash
pytest
ruff check .
```

## Planned pipeline

```text
generate -> local scoring -> App Store -> domains/RDAP -> GitHub -> web -> legal review
```
