import random
correct = 0
while True:
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    op = random.randint(1, 3)
    if op == 1:
        jung = num1 + num2
        mark = "+"
        
    question = "%d X %d = ? " % (num1, num2)
    answer = int(input(question))
    if answer == jung:
        print("correct")
        correct = correct + 1
    else:
        print("wrong")
        print("do it again")
    