from __future__ import annotations

import csv
from pathlib import Path

import typer

from .generator import generate_names
from .scoring import rank_names

app = typer.Typer(no_args_is_help=True, help="Generate and rank brand-name candidates.")


@app.command()
def generate(
    count: int = typer.Option(200, min=1, help="Number of candidates to generate."),
    top: int = typer.Option(40, min=1, help="Number of ranked candidates to export."),
    seed: int = typer.Option(42, help="Seed for reproducible output."),
    output: Path = typer.Option(Path("candidates.csv"), help="CSV output path."),
) -> None:
    """Generate names, rank them, and write the best candidates to CSV."""
    names = generate_names(count=count, seed=seed)
    ranked = rank_names(names)[: min(top, count)]

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "rank",
                "name",
                "score",
                "pronunciation",
                "memorability",
                "warmth",
                "distinctiveness",
                "spelling_clarity",
            ]
        )
        for rank, candidate in enumerate(ranked, start=1):
            writer.writerow(
                [
                    rank,
                    candidate.name,
                    candidate.score,
                    candidate.pronunciation,
                    candidate.memorability,
                    candidate.warmth,
                    candidate.distinctiveness,
                    candidate.spelling_clarity,
                ]
            )

    typer.echo(f"Wrote {len(ranked)} ranked candidates to {output}")


if __name__ == "__main__":
    app()
