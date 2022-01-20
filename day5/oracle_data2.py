## 커서에 접근하는 코드를 함수로 작성

import cx_Oracle as ora


def myconn(): 
    dsn = ora.makedsn('localhost',1521,service_name='orcl')   ## 어디에 접속할 것인가 
    conn = ora.connect(user='scott', password= 'tiger', dsn=dsn, encoding='UTF-8') ## 계정 접속
    return conn


def getAllDate(conn): # conn객체를 매개변수 받아서 쿼리를 실행할 변수
    cur = conn.cursor()
    query = 'SELECT * FROM emp'
    for row in cur.execute(query):
        print(row)


def getNameAndJobData(conn):
    cur = conn.cursor()
    query = 'SELECT  ename, job from emp'
    cur.execute(query) # 실행
    while True:
        row = cur.fetchone() # 한 row (레코드) 읽기
        if row is None:
            break
        else:
            print(row)

def getDeptName(conn, no, name, ):
    cur = conn.cursor()
    query = f'SELECT * FROM dept Where deptno = {no}'  ## 모든 프로그래밍은 0부터 DB는 1부터 시작
    cur.execute(query)
    row = cur.fetchone()
    print(row)

    



if __name__ == '__main__' : # 메인 프로그램이 되어 프로그램이 시작된다? 

    print('emp 테이블 쿼리 조회가 시작합니다\n')
    
    scott_con = myconn()
    
    getAllDate(scott_con)
    
    no = input('dept 테이블에서 검색할 부서번호(deptno)를 입력하세요:')
    print(f'{no} 번호의 부서명')
    
    getDeptName(scott_con, no)
    print('모든 쿼리 조회를 마쳤습니다')
    
    # getDeptName(scott_con)