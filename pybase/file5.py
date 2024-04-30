#파일 읽기
try:
    f = open("/Users/yeryeongseo/desktop/test.txt", "r")
    while True:
        txt = f.read(10)
        if len(txt) == 0: break
        print(txt, end ='')   
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close()
    


