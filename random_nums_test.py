from random_nums import get_random_num
import matplotlib.pyplot as plt

def histogram():
#check for uniform distribution
    random_values = []
    distribution = {}
    number_limit = 10
    for i in range(number_limit):
        distribution[i] = 0
    for i in range(100):
        num = get_random_num(number_limit)
        random_values.append(num)
        distribution[num] += 1
    print(random_values)
    print(distribution)

#def repetition_check():
#   check for repition

def main():
    histogram()

main()
