class Farkle:

    def score(self, array_of_dice):
        turn_score = 0
        for dice in array_of_dice:
            turn_score = self.__score_single_dice(dice, turn_score)
        turn_score = self.__score_triple_dice(array_of_dice, turn_score)
        return turn_score

    def __score_triple_dice(self, array_of_dice, turn_score):
        if array_of_dice.count(3) == 3:
            turn_score += 300
        return turn_score

    def __score_single_dice(self, dice, turn_score):
        if dice == 1:
            turn_score += 100
        if dice == 5:
            turn_score += 50
        return turn_score
