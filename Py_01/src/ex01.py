from typing import Dict
import ex00


def decorator_add(func):
    def wrapper(*args, **kwargs):
        purse: Dict[str, int] = {}
        num_ingots = func(*args, **kwargs)
        for _ in range(num_ingots):
            purse = ex00.add_ingot(purse)
        return purse
    return wrapper


@decorator_add
def add_num_ignots(num: int):
    return num


def split_booty(*purses: Dict[str, int]) -> Dict[str, int]:
    num_gold = 0
    for purse in purses:
        num_gold += purse.get('gold_ingots', 0)
    if num_gold > 0:
        num = num_gold // 3
        result1 = add_num_ignots(num)
        result2 = add_num_ignots(num)
        result3 = add_num_ignots(num)
        if num_gold % 3 == 1:
            result3 = add_num_ignots(num + 1)
        elif num_gold % 3 == 2:
            result2 = add_num_ignots(num + 1)
            result3 = add_num_ignots(num + 1)
    return (result1, result2, result3)


if __name__ == "__main__":
    purse1: Dict[str, int] = {'silver_ingots': 1, 'trash': 6}
    purse2: Dict[str, int] = {'silver_ingots': 2, 'gold_ingots': 11}
    purse3: Dict[str, int] = {'silver_ingots': 3, 'gold_ingots': 3}
    purse4: Dict[str, int] = {'silver_ingots': 4, 'gold_ingots': 4}
    purse5: Dict[str, int] = {'cheburek': 4, 'gold_ingots': 0}
    print(
        split_booty(
            purse1,
            purse2,
            purse3,
            purse4,
            purse5))
