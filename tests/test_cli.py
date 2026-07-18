from __future__ import annotations

import csv
from pathlib import Path

from typer.testing import CliRunner

from brand_name_finder.cli import app

runner = CliRunner()


def test_cli_writes_ranked_csv(tmp_path: Path) -> None:
    output = tmp_path / "results" / "candidates.csv"

    result = runner.invoke(
        app,
        [
            "--count",
            "12",
            "--top",
            "5",
            "--seed",
            "7",
            "--output",
            str(output),
        ],
    )

    assert result.exit_code == 0, result.output
    assert output.exists()
    assert "Wrote 5 ranked candidates" in result.output

    with output.open(newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))

    assert rows[0] == [
        "rank",
        "name",
        "score",
        "pronunciation",
        "memorability",
        "warmth",
        "distinctiveness",
        "spelling_clarity",
    ]
    assert len(rows) == 6
    assert [row[0] for row in rows[1:]] == ["1", "2", "3", "4", "5"]
