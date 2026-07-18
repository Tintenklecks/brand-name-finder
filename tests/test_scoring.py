from brand_name_finder.scoring import rank_names, score_name


def test_score_is_bounded() -> None:
    candidate = score_name("Lunera")
    assert 0 <= candidate.score <= 100


def test_ranking_is_descending() -> None:
    ranked = rank_names(["Lunera", "Qxyzz", "Mavio"])
    assert [item.score for item in ranked] == sorted((item.score for item in ranked), reverse=True)


def test_common_startup_suffix_is_penalized() -> None:
    assert score_name("Norio").distinctiveness < score_name("Norel").distinctiveness
