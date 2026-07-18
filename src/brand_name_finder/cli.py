from __future__ import annotations

import csv
from pathlib import Path
from typing import Annotated

import typer

from .generator import generate_names
from .scoring import rank_names

app = typer.Typer(no_args_is_help=True, help="Generate and rank brand-name candidates.")


@app.command()
def generate(
    count: Annotated[
        int,
        typer.Option(min=1, help="Number of candidates to generate."),
    ] = 200,
    top: Annotated[
        int,
        typer.Option(min=1, help="Number of ranked candidates to export."),
    ] = 40,
    seed: Annotated[
        int,
        typer.Option(help="Seed for reproducible output."),
    ] = 42,
    output: Annotated[
        Path,
        typer.Option(help="CSV output path."),
    ] = Path("candidates.csv"),
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
