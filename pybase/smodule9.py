import random
food = ["pizza", "wings", "ramen-noodles", "hanburger", "boba"]
print(random.smaple(food, 2))
lotto = random.sample(range(1, 46),6)
lotto.sort()
print(lotto)