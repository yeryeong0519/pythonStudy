#리스트 컴프리헨션 : 리스트 안의 요소가 수열형태일때는 일일이 나열 할 필요 없이 생성
nums = [n for n in range(1, 11)]
print(nums)
nums2 = [n * 2 for n in range(1, 11)]
print(nums2)
nums3 = [5, 8, 3, 10, 9]
nums3.sort()
print(nums3)
str1 = ['b', 'c', 'f', 'a', 'k']
str1.sort()
str1.reverse()
print(str1)
nums4 = [23, 45, 96, 63, 12]
print(nums4.index(96))