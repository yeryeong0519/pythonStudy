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
    id = 1
    sql = '''
    UPDATE student_tbl SET name = "홍길순", address = "서울시 중구" where id = %d
    ''' % id
    
    
    with db.cursor() as cursor:
        cursor.execute(sql)
except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close() 