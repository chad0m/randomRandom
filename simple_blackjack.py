from random import random
import random_nums

class simple_blackjack:
    '''give integer 0-int]'''
    def __init__(self) -> None:
        print("Welcome to blackjack")
        print(random_nums.get_random_num(10))

if __name__ == '__main__':
    i = simple_blackjack()