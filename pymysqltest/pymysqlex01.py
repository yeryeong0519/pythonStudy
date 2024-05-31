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
    sql = '''
    CREATE TABLE student_tbl(id int primary key auto_increment not null,
    name varchar(20), age int, address varchar(50))
    ENGINE = InnoDB DEFAULT CHARSET = utf8
    '''
    with db.cursor() as cursor:
        cursor.execute(sql)
except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close()