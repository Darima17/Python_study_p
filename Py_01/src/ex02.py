from typing import Dict
import ex00


def squeak_decorator(func):
    def wrapper(*args, **kwargs):
        print("SQUEAK")
        return func(*args, **kwargs)
    return wrapper


add_ingot = squeak_decorator(ex00.add_ingot)
get_ingot = squeak_decorator(ex00.get_ingot)
empty = squeak_decorator(ex00.empty)

if __name__ == "__main__":
    purse: Dict[str, int] = {'silver_ingots': 2, 'gold_ingots': 1}
    print(add_ingot(purse))
    print(get_ingot(purse))
    print(empty(purse))
