"""Planning a tea party as the first program in COMP 110"""

__author__ = "730483620"


def main_planner(guests: int) -> None:
    """Entrypoint of program"""
    print("A Cozy Tea Party for " + str(guests) + " People")
    print(" Tea Bags: " + str(tea_bags(guests)))
    print(" Treats: " + str(treats(guests)))
    print(" Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Calculates the number of tea bags per guest"""
    return people * 2


def treats(people: int) -> int:
    """Calculates the number of treats needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Caculates the cost of tea bags and treats combined"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input()))
