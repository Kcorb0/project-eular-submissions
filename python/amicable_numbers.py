
def check_amicable(num):
    
    proper_divs1 = []
    proper_divs2 = []

    for i in range(1, num):
        if num % i == 0:
            proper_divs1.append(i)
        
    for i in range(1, sum(proper_divs1)):
        if sum(proper_divs1) % i == 0:
            proper_divs2.append(i)

    if sum(proper_divs2) == num:
        return num
    else:
        return 0

amics = []

for i in range(200, 8000):
    amics.append(check_amicable(i))

print([i for i in amics if i != 0])
print(sum([i for i in amics if i != 0])-496)
