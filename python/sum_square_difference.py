
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

nums = range(101)
sum_squares = sum([n ** 2 for n in nums])
square_sum = sum(nums) ** 2

print(square_sum - sum_squares)
