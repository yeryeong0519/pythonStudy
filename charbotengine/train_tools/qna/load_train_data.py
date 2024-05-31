import sys
sys.path.append(r"D:\주간yw\pythonStudy\chatbotengine")
import pymysql
import openpyxl   #엑셀파일 읽어오기
from config.DataBaseConfig import * #DB접속 정보 불러오기

#학습 데이터 초기화 
def all_clear_train_data(db):
    #기본 학습 데이터 삭제 
    sql = '''
       DELETE FROM chatbot_train_data_tbl
    '''
    with db.cursor() as cursor :
         cursor.execute(sql)
    # auto increment 초기화
    sql='''
      ALTER TABLE chatbot_train_data_tbl AUTO_INCREMENT=1
    '''
    with db.cursor() as cursor :
        cursor.execute(sql)
        
        
# 엑셀에 있는 데이터를 한행씩 불러와서 db에 데이터 저장
def insert_data(db, xls_row):
    intent, ner, query, answer, answer_img_url=xls_row
    sql='''
        INSERT INTO chatbot_train_data_tbl(intent,ner,query,answer,answer_image)
        values('%s','%s','%s','%s','%s')
    ''' % (intent.value, ner.value, query.value, answer.value, answer_img_url.value)
    #엑셀에서 불러온 cell에 데이터가 없는 경우, null로 치환
    sql=sql.replace("None","null")
    with db.cursor() as cursor:
        cursor.execute(sql)
        print('{}저장'.format(query.value))
        db.commit()
train_file=r"D:\주간yw\pythonStudy\chatbotengine\train_tools\qna\train_data.xlsx"
db=None
try: 
        db=pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8'
        )
        #기존 학습 데이터 초기화
        all_clear_train_data(db)
        #학습 엑셀 파일 불러오기
        wb=openpyxl.load_workbook(train_file)
        sheet=wb['Sheet1']
        for row in sheet.iter_rows(min_row=2): #헤더는 불러오지 않음
            insert_data(db,row)
        wb.close()
except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close();

# #챗봇 엔진의 핵심 기능
# 1. 질문의도분류 :화자의 질문 의도를 파악
# 2. 개체명 인식:화자의 질문에 단어 토큰별 개체명을 인식
# 3. 핵심키워드 추출 : 화자의 질문 의미에서 핵심이 될 만한 단어 토큰을 추출
# 4. 답변 검색: 해당 질문 의도, 개체명, 핵심 키워드 등을 기반으로 답변을 학급 DB검색
# 5. 소켓 서버: 챗봇 엔진 서버