#파일 입출력



# 특정 경로에 파일 생성
# f = open('C:\\sources\\studypython\\test.txt','w')
# f.close()
# print('파일이 생성되었습니다')

# 특정 경로에 파일 읽어오기

f = open('test.txt','r', encoding='utf-8')
while True:
    line = f.readline()   # 텍스트 안에 글짜를 읽는다
    if not line:
        break
    print(line)

f.close()