str = "75"
try:
    
    score = int(str)
    if score >= 80:
        print("hakgyuk")
    else:
        print("bulhapgyuk")
except:
    print("점수 형식이 잘못되었습니다.")
print("finish")