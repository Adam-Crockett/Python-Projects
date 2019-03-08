import random

a = random.sample(range(100), 20)
b = random.sample(range(100), 50)

print([x for x in set(a) if x in b])
