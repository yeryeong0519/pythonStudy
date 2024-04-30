#파일 읽기
try:
    f = open("/Users/yeryeongseo/desktop/address.txt", "w")
    txt= f.read()
    print(txt)      
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close()
    


