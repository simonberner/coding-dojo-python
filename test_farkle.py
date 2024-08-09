from farkle import Farkle


# Test for a 1, Three 3s and a 5
def test_dice_combination1():
    items = [1, 2, 3, 3, 3, 5]
    farkle = Farkle()
    current_score = farkle.score(items)
    assert current_score == 450
