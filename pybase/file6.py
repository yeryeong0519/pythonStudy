#파일 읽기
try:
    f = open("/Users/yeryeongseo/desktop/test.txt", "r")
    lines = f.readlines()
    for line in lines:
        print(line)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close()
    


