try:
    age = int(input("let us know your age!>>"))
except:
    print("not good")
else:
    if age <= 18:
        print("under age cannot enter")
    else:
        print("welcome!")