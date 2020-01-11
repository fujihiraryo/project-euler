import numpy as np

a = 1
b = 1
x = 1
count = 2
while x < 1000:
    count += 1
    a, b, x = b, a + b, len(str(a+b))

print(count)
