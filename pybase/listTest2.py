score = [88, 90, 70, 60, 100, 75, 82, 50]
pos = score.index(100)
print("만점 받은 학생은" + str(pos + 1) + "번입니다.")
print("최고 점수는 %d점입니다." % max(score))