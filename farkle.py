class Farkle:

    def score(self, array_of_dice):
        turn_score = self.__score_five_of_a_kind(array_of_dice)
        array_of_dice = self.__remove_five_of_a_kind_dice(array_of_dice)
        turn_score += self.__score_four_of_a_kind(array_of_dice)
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
        score_map = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
        for dice_value, score in score_map.items():
            if array_of_dice.count(dice_value) == 3:
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
                return score
        return 0

    def __remove_fourofakind_dice(self, array_of_dice):
        four_of_a_kind_to_check = [1, 2, 3, 4, 5, 6]
        for dice_value in four_of_a_kind_to_check:
            if array_of_dice.count(dice_value) == 4:
                array_of_dice = [x for x in array_of_dice if x != dice_value]
        return array_of_dice

    def __score_five_of_a_kind(self, array_of_dice):
        score_map = {1: 4000, 2: 800, 3: 1200, 4: 1600, 5: 2000, 6: 2400}
        for value, score in score_map.items():
            if array_of_dice.count(value) == 5:
                return score
        return 0

    def __remove_five_of_a_kind_dice(self, array_of_dice):
        four_of_a_kind_to_check = [1, 2, 3, 4, 5, 6]
        for dice_value in four_of_a_kind_to_check:
            if array_of_dice.count(dice_value) == 5:
                array_of_dice = [x for x in array_of_dice if x != dice_value]
        return array_of_dice
