import random
for i in range(5):
    #print(random.random())
    print(random.randint(1, 10))
    
food = ["pizza", "wings", "ramen-noodles", "hanburger", "boba"]
print(random.choice(food))
#print(food)
food1 = random.shuffle(food)
print(food1)