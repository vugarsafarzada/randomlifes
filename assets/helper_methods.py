import random


def randomNumberBetween(lower: int, upper: int) -> int:
    return random.randint(lower, upper)


def randomBoolean() -> bool:
    possibility = randomNumberBetween(0, 1)
    return possibility == 1


def randomItemFromList(itemList: list) -> tuple:
    index = randomNumberBetween(0, len(itemList) - 1)
    return itemList[index]


def combineLists(list1: list, list2: list) -> list:
    combined_list = list(set(list1).union(list2))
    return combined_list
