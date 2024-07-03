##Robert Fernandez
##Complete
##Generate a 9 digit random lottery number.


import random

DIGITS = 7
MAX_LOTTERY_NUMBER = 9

def main():
    lottery_number = [0] * DIGITS
    for index in range(DIGITS):
        random_number = random.randint(0, MAX_LOTTERY_NUMBER)
        lottery_number[index] = random_number
    for number in lottery_number:
        print(number)


if __name__ == "__main__":
    main()
