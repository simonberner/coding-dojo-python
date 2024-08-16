from multiprocessing.connection import arbitrary_address


class Farkle:

    def score(self, array_of_dice):
        turn_score = self._score_four_of_a_kind(array_of_dice)
        array_of_dice = self.__remove_fourofakind_dice(array_of_dice)
        turn_score = self.__score_triple_dice(array_of_dice, turn_score)
        array_of_dice = self.__remove_triple_dice(array_of_dice)
        for dice in array_of_dice:
            turn_score = self.__score_single_dice(dice, turn_score)
        return turn_score

    def __remove_triple_dice(self, array_of_dice):
        triple_dice_to_check = [1, 2, 3, 4, 5, 6]
        for dice_value in triple_dice_to_check:
            if array_of_dice.count(dice_value) == 3:
                # create a new list containing only those elements x that satisfy the condition x != dice_value.
                array_of_dice = [x for x in array_of_dice if x != dice_value]
        return array_of_dice

    def __score_triple_dice(self, array_of_dice, turn_score):
        if array_of_dice.count(1) == 3:
            turn_score += 1000
        if array_of_dice.count(2) == 3:
            turn_score += 200
        if array_of_dice.count(3) == 3:
            turn_score += 300
        if array_of_dice.count(4) == 3:
            turn_score += 400
        if array_of_dice.count(5) == 3:
            turn_score += 500
        if array_of_dice.count(6) == 3:
            turn_score += 600
        return turn_score

    def __score_single_dice(self, dice, turn_score):
        if dice == 1:
            turn_score += 100
        if dice == 5:
            turn_score += 50
        return turn_score

    def _score_four_of_a_kind(self, array_of_dice):
        score = 0
        if array_of_dice.count(1) == 4:
            score = 2000
        if array_of_dice.count(3) == 4:
            score = 600
        return score

    def __remove_fourofakind_dice(self, array_of_dice):
        four_of_a_kind_to_check = [1, 2, 3, 4, 5, 6]
        for dice_value in four_of_a_kind_to_check:
            if array_of_dice.count(dice_value) == 4:
                array_of_dice = [x for x in array_of_dice if x != dice_value]
        return array_of_dice
