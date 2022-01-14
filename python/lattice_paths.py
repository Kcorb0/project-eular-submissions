
# Travel distance is double the grid size
# 5x5 grid will always take 10 steps no matter which way
# In the case of a 5x5 grid, you have to go left 5 and down 5, a metter of chaning the order
# Aka 5 choose 5 

size1 = list(range(40, 19, -1))
size2 = list(range(20, 0, -1))

x = 40
y = 40

for i in size1:
    x = x*i

for n in size2:
    y = y*n

print(x)
print(y)
print(x/y)