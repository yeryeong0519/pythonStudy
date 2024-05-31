import pymysql

db=None
try:
    #DB연결 정보
    db = pymysql.connect(
      host = '127.0.0.1',
      user = 'root',
      passwd = '1234',
      db = 'chatbotdb',
      charset = 'utf8'
   )
    
    #데이터 삭제
    id = 3 # 데이터 id
    sql = '''
   DELETE from tb_student where id = %d
    ''' % id

    # 테이블 생성
    with db.cursor() as cursor:
        cursor.execute(sql)
        db.commit()

except Exception as e:
    print(e)
finally: 
    if db is not None:
        db.close()