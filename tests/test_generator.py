import pytest

from brand_name_finder.generator import generate_names, is_valid


def test_generation_is_reproducible() -> None:
    assert generate_names(25, seed=7) == generate_names(25, seed=7)


def test_generated_names_are_unique_and_valid() -> None:
    names = generate_names(100, seed=11)
    assert len(names) == len(set(names)) == 100
    assert all(is_valid(name) for name in names)


def test_count_must_be_positive() -> None:
    with pytest.raises(ValueError):
        generate_names(0)
