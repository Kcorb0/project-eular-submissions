# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.



# Function

def self_powers(n):

    return sum([x**x for x in range(1, n+1)])

print(self_powers(1000))


# One line
print(str(sum([x**x for x in range(1, 1001)]))[-10:])