첫번째 = '투'
두번째 = '유'
str1 = "I'm so happy {0} U. are {1}?".format(첫번째,두번째) 
print(str1)



str2 = f"I'm so happy {첫번째} U. are {두번째}?"
print(str2)

money = 1000000000
print(format(money, ',d'))

from datetime import datetime

now = datetime.now() 
print(now)
print(now.strftime('%Y년 %m월 %d일 %H:%M:%S'))



import math
mypi = math.pi

print(mypi)
print('{0}'.format(mypi))
print('{0:0.2f}'.format(mypi))
print(f'{mypi:0.6f}')



full_name = 'Hugo MG Sung'

age = 47
gretting = '''안녕하세요. 저는 {full_name}입니다. 나이는 {age:0.2f}살 이고요 .
'''
print(gretting)


part_name = full_name.split(',')
print(type(part_name))
print(part_name)


code = 'TEST|2022|01|17|F45678'
split_codes = code.split('|')
print(split_codes)


print(full_name.replace('Hugo MG','Ashley'))
