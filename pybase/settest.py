mammal = {"코끼리", "고릴라", "사자", "고래", "사람", "원숭이", "개"}
primate = {"사람", "원숭이", "고릴라"}
if "사자" in mammal:
    print("포유류입니다.")
else:
    print("포유류가 아닙니다.")

print(primate <= mammal)    #부분집합
print(primate < mammal)     #진성부분집합
print(primate <= primate)   #포함집합
print(primate < primate)    #진성포함집합
