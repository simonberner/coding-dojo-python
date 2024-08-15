from farkle import Farkle


# Test for a 1, Three 3s and a 5
def test_dice_combination1():
    items = [1, 2, 3, 3, 3, 5]
    farkle = Farkle()
    current_score = farkle.score(items)
    assert current_score == 450


# Test for a Three 1s and Three 2s
def test_dice_combination2():
    items = [1, 1, 1, 2, 2, 2]
    farkle = Farkle()
    current_score = farkle.score(items)
    assert current_score == 1200


# Test for Three 4s, a 6, a 1, a 5
def test_dice_combination3():
    items = [4, 4, 4, 6, 1, 5]
    farkle = Farkle()
    current_score = farkle.score(items)
    assert current_score == 550


# Test for Three 5s and Three 6s
def test_dice_combination4():
    items = [6, 6, 6, 5, 5, 5]
    farkle = Farkle()
    current_score = farkle.score(items)
    assert current_score == 1100


# Test Four-of-a-kind (triple score is multiplied  by 2)
def test_four_threes():
    dice = [3, 3, 3, 3, 1, 5]
    farkle = Farkle()
    score = farkle.score(dice)
    assert score == 750
