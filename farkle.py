class Farkle:

    def score(self, array_of_dice):
        turn_score = self.__score_six_of_a_kind(array_of_dice)
        turn_score += self.__score_five_of_a_kind(array_of_dice)
        turn_score += self.__score_four_of_a_kind(array_of_dice)
        turn_score = self.__score_triple_dice(array_of_dice, turn_score)
        turn_score += self.__score_three_different_pairs(array_of_dice)
        turn_score += self.__score_straight(array_of_dice)
        for dice in array_of_dice:
            turn_score = self.__score_single_dice(dice, turn_score)
        return turn_score

    def __score_triple_dice(self, array_of_dice, turn_score):
        score_map = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
        for dice_value, score in score_map.items():
            if array_of_dice.count(dice_value) == 3:
                if len(array_of_dice) == 3:
                    array_of_dice[:] = []
                if len(array_of_dice) > 3:
                    while dice_value in array_of_dice:
                        array_of_dice.remove(dice_value)
                turn_score += score
        return turn_score

    def __score_single_dice(self, dice, turn_score):
        if dice == 1:
            turn_score += 100
        if dice == 5:
            turn_score += 50
        return turn_score

    def __score_four_of_a_kind(self, array_of_dice):
        score_map = {1: 2000, 2: 400, 3: 600, 4: 800, 5: 1000, 6: 1200}
        for value, score in score_map.items():
            if array_of_dice.count(value) == 4:
                if len(array_of_dice) == 4:
                    array_of_dice[:] = []
                if len(array_of_dice) > 4:
                    while value in array_of_dice:
                        array_of_dice.remove(value)
                return score
        return 0

    def __score_five_of_a_kind(self, array_of_dice):
        score_map = {1: 4000, 2: 800, 3: 1200, 4: 1600, 5: 2000, 6: 2400}
        for value, score in score_map.items():
            if array_of_dice.count(value) == 5:
                # if 5 dice then remove all
                if len(array_of_dice) == 5:
                    array_of_dice[:] = []
                # if 6 dice then remove just the 5
                if len(array_of_dice) == 6:
                    # remove all the dice in the array with the value
                    while value in array_of_dice:
                        array_of_dice.remove(value)
                return score
        return 0

    def __score_six_of_a_kind(self, array_of_dice):
        score_map = {1: 8000, 2: 1600, 3: 2400, 4: 3200, 5: 4500, 6: 4800}
        for value, score in score_map.items():
            if array_of_dice.count(value) == 6:
                array_of_dice[:] = []
                return score
        return 0

    def __score_three_different_pairs(self, array_of_dice):
        dice_to_check = [1, 2, 3, 4, 5, 6]
        array_of_dice_new = array_of_dice
        pairs = 0
        for dice in dice_to_check:
            if array_of_dice_new.count(dice) == 2:
                pairs += 1
                # remove the dice from the array
                array_of_dice_new = [x for x in array_of_dice_new if x != dice]
        if pairs == 3:
            # only if there are three different pairs we slice and thus assign the new array to the original array
            array_of_dice[:] = array_of_dice_new
            return 800
        return 0

    def __score_straight(self, array_of_dice):
        dice_to_check = [1, 2, 3, 4, 5, 6]
        if sorted(array_of_dice) == dice_to_check:
            array_of_dice[:] = []
            return 1200
        return 0
