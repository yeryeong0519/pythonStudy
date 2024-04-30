#파일 읽기
try:
    f = open("/Users/yeryeongseo/desktop/address.txt", encoding = "utf-8",)
    while True:
        txt = f.readline()
        if not txt : break
        
        print(txt)      
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close()
    


