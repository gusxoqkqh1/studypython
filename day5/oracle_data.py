# oracle_data



import cx_Oracle as ora

dsn = ora.makedsn('localhost',1521, service_name='orcl')
#connect(user, password, dsn, encoding)
conn = ora.connect(user='scott',password='tiger',dsn=dsn, encoding='utf-8')

cur = conn.cursor()

try:
    for row in cur.execute('SELECT * FROM emp;'):
        print(row)   


except ora.DatabaseError as e:
    print(f'쿼리문이 잘못되었습니다. 13번 라인 확인요: {e}')

finally:


    cur.close()   # 커서 닫고
    conn.close()  # 접속 닫음 