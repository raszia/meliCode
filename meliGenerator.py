#!/usr/bin/python3
import random
import sys


def meli_code_generator():
    while True:
        meli_code = random.sample(range(1, 10), 9)
        place_list = [10,9,8,7,6,5,4,3,2]

        x = 0
        for (a, b) in zip(place_list, meli_code): 
            x = x + (a*b)

        remainder = (x % 11)

        if x < 2:
            last_number = remainder
        elif x >= 2:
            last_number = (11 - remainder)

        if last_number < 10:
            listToStr = ' '.join([str(number) for number in meli_code])
            print(listToStr.replace(" ","")+str(last_number))  
            break
        else:
            pass

if __name__ == "__main__":
    meli_code_generator()