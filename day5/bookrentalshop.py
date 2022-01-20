# bookrentalshop
# divbl, memberbl


from __future__ import division
import cx_Oracle as ora

def myconn():
    dsn = ora.makedsn('localhost',1521,service_name='orcl')
    conn = ora.connect(user='scott',password='tiger',dsn=dsn, encoding='utf-8')
    return conn


# 1번 
def getAlldatafromDivtbl(conn):
    cur = conn.cursor()
    query = 'SELECT * FROM divtbl'
    for row in cur.execute(query):
        print(row)

# 2번 
### 컬럼 추가
def setDataIntoDivtbl(conn, tup):
    cur = conn.cursor()
    query = '''INSERT INTO divtbl (division, names) 
                VALUES (:1, :2)'''        # :1, :2   = 튜플 tup에 1번과 2번 (데이터베이스는 프로그래밍과 다르게 1번부터 시작한다)
    cur.execute(query, tup)
    cur.close()
    conn.commit()   # COMMIT;   < 컬럼을 추가한 후 COMMIT 을 하지 않으면 저장되지 않는다

# 3번 
def getsomeDataFromMembertbl(conn):
    cur = conn.cursor()
    query = '''SELECT names, levels, addr, mobile, email 
                FROM membertbl
                WHERE addr LIKE '서울%'
                AND UPPER(email) LIKE '%@NAVER.COM'
                ORDER BY idx DESC;'''
    for row in cur.execute(query):
        print(row)
    
    cur.close()


# 4번 membertbl에 신규회원 입력하기
def setNewMemberIntoMembertbl(conn,tub):
    cur = conn.cursor()
    qeury = '''SELECT ROWNUM, idx
                FROM (
                    SELECT idx FROM membertbl
                    ORDER BY idx DESC  
                      ) 
                WHERE ROWNUM = 1
            ''' 
    idx = cur.fetchone()[1]
    
    intup = (idx+1, tup[0],tup[1],tup[2],tup[3],)
    query = '''INSERT INTO membertbl 
                (idx, names, levels, userid, password)
                VALUES (:1, :2, :3, :4, :5)'''
    cur.execute(query, intup)
    conn.commit()
    cur.close() 


# 5번 
def setChangeMemberFromMembertbl(conn,tub):
    cur = conn.cursor()
    query = '''UPDATE membertbl
                SET   addr   = :1
                    , mobile = :2
                    , email  = :3
                WHERE idx    = :4
            '''

    cur.execute(query, tup) 
    cur.close()
    cur.commit()    
            
# 6번
def deleteDevision(conn,division):
    cur = conn.cursor()
    query = 'DELECT * FROM divtbl WHERE division =:1'
    cur.execute(query,division)
    conn.commit()



if __name__ == '__main__':
    
    # 1. divtbl에서 데이터를 조회
    print("책 대여점 프로그램 시작")
    scott_con = myconn() # db 접속
    print("책  장르 정보 조회 ")
    getAlldatafromDivtbl(scott_con)

    ## 2. divtbl에 새로운 데이터 입력
    print("책 장르 정보입력")
    division = input('구분코드 입력:')
    names = input('장르명 입력:')
    tup = (division,names)
    setDataIntoDivtbl(scott_con,tup)
    print('입력 정보 성공')

    ## 3. membertbl에서 데이터를 조회
    getsomeDataFromMembertbl(scott_con)
    

  ## 4. membertbl에서 데이터를 입력
    print('신규 회원 입력')
    name = input('이름입력:')
    levels = input('레벨입력(A~D):')
    userid = input('아이디입력(최대20자):')
    password = input('패스워드입력(최대20자):')
    tup = (name,levels,userid,password) 
    setNewMemberIntoMembertbl(scott_con, tup)


    ## 5. membertbl 새 데이터를 수정
    print('기존회원 수정')
    idx = input('변경회원번호:')
    addr = input('주소 입력: ')
    mobile = input('폰 번호 입력(-포함)')
    email = input('이메일 입력:')
    tup = (addr, mobile, email, idx)

    setChangeMemberFromMembertbl(scott_con,tup)
    print('기존회원 수정완료')


    ## 6. divtbl에 임의 데이터 삭제 
    
    print('책 장르정보 삭제:')
    division = input('삭제할 장르코드 입력')
    deleteDevision(scott_con, division)
    print('삭제 성공')