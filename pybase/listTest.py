score=[[88,75,96,84,60],[50,78,95,92,70,],[75,84,86,60,99]]
tot=0
totsub=0
num=1
for student in score:
    sum=0
    for subject in student:
        sum+=subject #sum=sum+subject
    # print(num+ "번 학생 총점 : "+sum)
    print("%d번 학생 총점 %d, 평균 %.2f" % (num, sum, sum/len(student)))
    num+=1
    tot+=sum
    totsub+=len(student)
print("반 평균 %.2f" %(tot/totsub))