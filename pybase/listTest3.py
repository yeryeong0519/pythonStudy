score = [88, 90, 70, 60, 100, 75, 82, 50]
score.remove(70)
print(score)
score.pop()
print(score)
score.pop(4)
print(score)
nums = [12, 50, 23, 12, 5, 10]
print(nums.count(12))
ans = input("결제하시겠습니까?")
if ans in["yes", "y", "ok", "예", "당근"]:
    print("구입해주셔서 고맙습니다.")
else:
    print("안녕히가세요")