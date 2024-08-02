from typing import Dict


def add_ingot(purse: Dict[str, int]) -> Dict[str, int]:
    new_purse = purse.copy()
    new_purse['gold_ingots'] = new_purse.get('gold_ingots', 0) + 1
    return new_purse


def get_ingot(purse: Dict[str, int]) -> Dict[str, int]:
    if 'gold_ingots' in purse and purse['gold_ingots'] > 0:
        new_purse = purse.copy()
        new_purse['gold_ingots'] -= 1
        return new_purse
    else:
        return {}


def empty(purse: Dict[str, int]) -> Dict[str, int]:
    return {}


if __name__ == "__main__":
    purse: Dict[str, int] = {'silver_ingots': 2, 'gold_ingots': 1}
    # print('exemple empty function: ', empty(purse))
    # print('exemple get_ingot function: ', get_ingot(purse))
    # print('exemple add_ingot function: ', add_ingot(purse))

    print(add_ingot(get_ingot(add_ingot(empty(purse)))))
