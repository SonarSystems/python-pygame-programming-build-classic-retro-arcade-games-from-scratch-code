class Economy:
    def __init__(self, starting_gold):
        self.gold = starting_gold

    def can_afford(self, cost):
        return self.gold >= cost

    def spend(self, amount):
        self.gold -= amount

    def earn(self, amount):
        self.gold += amount
