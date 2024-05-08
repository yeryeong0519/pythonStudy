import random

correct = 0
count = 0

while count < 11:
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    question = "%d + %d = ? " % (num1, num2)
    answer = int(input(question))
    if answer == num1 + num2:
        print("correct")
        correct += 1
    else:
        print("wrong")
        print("do it again")
    count += 1

print("you've got %d questions correct" % correct)


