import pymysql
db = None
try:
    db = pymysql.connect(
        host = '127.0.0.1',
        user = 'root',
        passwd = 'danbi0519',
        db = 'chatbotdb',
        charset = 'utf8'
    )
    #테이블 생성
    sql = 'INSERT INTO student_tbl(name, age, address) values("홍길동", 30, "서울시 강남구")'
    
    with db.cursor() as cursor:
        cursor.execute(sql)
except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close()