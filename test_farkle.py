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
