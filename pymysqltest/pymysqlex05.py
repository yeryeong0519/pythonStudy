import pymysql
import pandas as pd

db = None
try:
    db = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='danbi0519',
        db='chatbotdb',
        charset='utf8'
    )
    print("DB 연결 성공")
    
    with db.cursor() as cursor:
        # 테이블 생성
        sql = '''
        CREATE TABLE IF NOT EXISTS student_tbl (
            id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
            name VARCHAR(20),
            age INT,
            address VARCHAR(50)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8
        '''
        cursor.execute(sql)
        print("테이블 생성 성공")
    
    # 데이터 여러 개 추가
    students = [
        {'name': '손흥민', 'age': 30, 'address': '서울시 마포구'},
        {'name': '서예령', 'age': 24, 'address': '서울시 강남구'},
        {'name': '박보검', 'age': 24, 'address': '서울시 서초구'},
        {'name': '류선재', 'age': 21, 'address': '수원시 권선구'},
        {'name': '보미', 'age': 24, 'address': '서울시 중구'}
    ]
    
    with db.cursor() as cursor:
        for s in students:
            sql = '''
            INSERT INTO student_tbl (name, age, address) VALUES (%s, %s, %s)
            '''
            cursor.execute(sql, (s['name'], s['age'], s['address']))
        db.commit()
        print("데이터 삽입 성공")
    
    # 나이가 cond_age 이상인 학생 조회
    cond_age = 40
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = '''
            SELECT * FROM student_tbl WHERE age >= %s
        '''
        cursor.execute(sql, (cond_age,))
        results = cursor.fetchall()
    print("나이가 %d 이상인 학생들:" % cond_age)
    print(results)
    
    # 이름으로 학생 조회
    cond_name = "박보검"
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = '''
            SELECT * FROM student_tbl WHERE name = %s
        '''
        cursor.execute(sql, (cond_name,))
        result = cursor.fetchone()
    if result:
        print("이름이 %s인 학생:" % cond_name)
        print(result['name'], result['age'])
    else:
        print("이름이 %s인 학생을 찾을 수 없습니다." % cond_name)
    
    # Pandas DataFrame으로 표현
    df = pd.DataFrame(results)
    print("Pandas DataFrame:")
    print(df)
except pymysql.MySQLError as e:
    print("MySQL 에러:", e)
except Exception as e:
    print("일반 에러:", e)
finally:
    if db is not None:
        db.close()
        print("DB 연결 종료")
