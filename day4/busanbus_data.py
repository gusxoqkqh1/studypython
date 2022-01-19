# 부산버스 노션별 이용건수

import csv

file_name = '부산버스정보.csv'
f = open(file_name, mode='r', encoding='utf-8')

reader = csv.reader(f, delimiter=',')     # delimiter 는 구분자이며, 각 단어당 ''로 구분하겠다

next(reader)  ## 헤더를 없애는 역학 첫번제 제목을 없앤다
for line in reader:
    print(line)

f.close()
