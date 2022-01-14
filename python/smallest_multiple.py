# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def evenly_divisible(max):

    num_range = range(1, max+1)
    lowest_mult = 2
    score = 0

    while True:
        for i in num_range:
            if lowest_mult % i == 0:
                score += 1
                if score == max:
                    return lowest_mult
            else:
                score = 0
                lowest_mult += 2

print(evenly_divisible(20))