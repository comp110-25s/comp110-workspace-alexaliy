"""File to define River class."""

__author__: str = "730483620"

from fish import Fish
from bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Animals pass away from old age"""
        self.fish = [f for f in self.fish if f.age <= 3]
        self.bears = [b for b in self.bears if b.age <= 5]

    def remove_fish(self, amount: int):
        """Fish removed from fishing"""
        self.fish = self.fish[amount:]

    def bears_eating(self):
        """Taking into account bear eating fish"""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self):
        """Taking into account if bear gets hungry"""
        self.bears = [b for b in self.bears if b.hunger_score >= 0]

    def repopulate_fish(self):
        """Taking into account fish births"""
        offspring = (len(self.fish) // 2) * 4
        self.fish += [Fish() for _ in range(offspring)]

    def repopulate_bears(self):
        """Taking into account bear births"""
        offspring = len(self.bears) // 2
        self.bears += [Bear() for _ in range(offspring)]

    def view_river(self):
        """Population of the river"""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Stimulate a week in the river"""
        for __ in range(7):
            self.one_river_day()
