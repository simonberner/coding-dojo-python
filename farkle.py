class Farkle:

    def score(self, array_of_dice):
        turn_score = 0
        for dice in array_of_dice:
            if dice == 1:
                turn_score += 100
            if dice == 5:
                turn_score += 50
        if array_of_dice.count(3) == 3:
            turn_score += 300
        return turn_score
