import pytest
from farkle import Farkle


# This fixture will be shared across the entire module.
@pytest.fixture(scope="module", autouse=True)
def farkle():
    global farkle  # Use a global variable to store the instance
    farkle = Farkle()


# Test for a 1, Three 3s and a 5
def test_dice_combination1():
    dice = [1, 2, 3, 3, 3, 5]
    assert farkle.score(dice) == 450


# Test for a Three 1s and Three 2s
def test_dice_combination2():
    dice = [1, 1, 1, 2, 2, 2]
    assert farkle.score(dice) == 1200


# Test for Three 4s, a 6, a 1, a 5
def test_dice_combination3():
    dice = [4, 4, 4, 6, 1, 5]
    assert farkle.score(dice) == 550


# Test for Three 5s and Three 6s
def test_dice_combination4():
    dice = [6, 6, 6, 5, 5, 5]
    assert farkle.score(dice) == 1100


# Test Four-of-a-kind (triple score is multiplied  by 2)
def test_four_threes():
    dice = [3, 3, 3, 3, 1, 5]
    assert farkle.score(dice) == 750


# Test Four-of-a-kind (triple score is multiplied by 2)
def test_four_ones():
    dice = [1, 1, 1, 1, 5, 5]
    assert farkle.score(dice) == 2100


# Test Five-of-a-kind (triple score is multiplied by 4)
def test_five_ones():
    dice = [1, 1, 1, 1, 1, 5]
    assert farkle.score(dice) == 4050


# Test Five-of-a-kind (triple score is multiplied by 4)
def test_five_six():
    dice = [6, 6, 6, 6, 6, 5]
    assert farkle.score(dice) == 2450


# Test Six-of-a-kind (triple score is multiplied by 8)
def test_six_six():
    dice = [6, 6, 6, 6, 6, 6]
    assert farkle.score(dice) == 4800


# Test 'Three Pairs'
def test_three_different_pairs():
    dice = [1, 1, 5, 5, 6, 6]
    assert farkle.score(dice) == 800
