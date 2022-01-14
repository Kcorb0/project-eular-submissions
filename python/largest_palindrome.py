# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


palindromes = []

for num1 in range(1000, 100, -1):
    for num2 in range(1000, 100, -1):
        product = str(num1*num2)
        
        if product == product[::-1]:
            palindromes.append(int(product))
            break

print(max(palindromes))