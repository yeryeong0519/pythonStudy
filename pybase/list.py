score=[88,90,70,82,96]
name=['홍길동','김철수','이영희']
namescore=['홍길동',90,'이영희',88,'김철수',95]
print(score[0])
sum=0
for s in score:
    sum+=s #sum=sum+s
print("총점=",sum)
print("평균=",sum/len(score))
m=[10,20,["홍길동","김철수"]]
print(m[-1])