from brand_name_finder.scoring import rank_names, score_name


def test_score_is_bounded() -> None:
    candidate = score_name("Lunera")
    assert 0 <= candidate.score <= 100


def test_ranking_is_descending() -> None:
    ranked = rank_names(["Lunera", "Qxyzz", "Mavio"])
    assert [item.score for item in ranked] == sorted((item.score for item in ranked), reverse=True)


def test_common_startup_suffix_is_penalized() -> None:
    assert score_name("Norio").distinctiveness < score_name("Norel").distinctiveness


def test_f_and_v_are_not_rewarded_as_warm_consonants() -> None:
    assert score_name("Famera").warmth == score_name("Kamera").warmth


def test_f_and_v_reduce_spelling_clarity() -> None:
    clear = score_name("Lamena")
    ambiguous = score_name("Famena")
    especially_ambiguous = score_name("Favena")

    assert (
        clear.spelling_clarity > ambiguous.spelling_clarity > especially_ambiguous.spelling_clarity
    )


def test_consonant_clusters_reduce_pronunciation_score() -> None:
    assert score_name("Fanama").pronunciation > score_name("Falnam").pronunciation


def test_clear_name_ranks_before_f_v_variant() -> None:
    assert rank_names(["Favena", "Lamena"])[0].name == "Lamena"
