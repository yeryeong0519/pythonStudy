# ner:개체명 , 개체명이 없는경우 null
# query:질문 테스트
# answer:답변 테스트
# answer_image: 답변에 들어갈 이미지 


import sys
sys.path.append("D:\주간yw\pythonStudy\chatbotengine")
print(sys.path)
import pymysql
from config.DataBaseConfig import * #DB접속 정보 불러오기 
db=None
try:
    db=pymysql.connect(
       host=DB_HOST,
       user=DB_USER,
       passwd=DB_PASSWORD,
       db=DB_NAME,
       charset='utf8'
    )
    #챗봇 학습 데이터 테이블 생성
    sql='''
        CREATE TABLE IF NOT EXISTS chatbot_train_data_tbl(
            id INT UNSIGNED NOT NULL AUTO_INCREMENT,
            intent VARCHAR(45) NULL,
            ner VARCHAR(1024) NULL,
            query TEXT NULL,
            # TEXT는 크기가 아주 큰 값 가능 VARCHAR은 적은값만 
            answer   TEXT NOT NULL,
            answer_image VARCHAR(2048) NULL,
            PRIMARY KEY(id))
            ENGINE=InnoDB DEFAULT CHARSET=utf8
    '''
    with db.cursor() as cursor:
        cursor.execute(sql)
except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close()
