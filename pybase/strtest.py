s = "python"
print(s[2])
print(s[-2])
print(s[2:5])
print(s[3:])
print(s[:4])
print(s[2:-2])
file = "20240422-144720.jpg"
print("촬영날짜 :" + file[:4] + "년" + file[4:6] + "월" + file[6:8] + "일")
print("촬영시간 :" + file[9:11] + "시" + file[11:13] + "분")
print("이미지 종류 : " + file[-3:])
week = "월화수목금토일"
print(week[::2])    #[start:end:step]
print(week[::2])
print(week[::-1])
