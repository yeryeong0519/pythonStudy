asia = {"korea", "china", "japan"}
asia.add("vietnam") #add
asia.add("china")
asia.remove("japan")
print(asia)
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1.intersection(s2))
print(s1 | s2)
print(s1.union(s2))
print(s1-s2)
print(s2-s1)
print(s1^s2)
# & 교집합 : 두 집합에 모두 있는 원소
# | 합집합 : 두 집합의 모든 원소
# - 차집합 : 왼쪽 집합의 원소 중 오른쪽 집합의 원소를 뺀것
# ^ 배타적집합 : 한 쪽 집합에만 있는 원소의 합 
