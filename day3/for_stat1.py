# # 기본 for 문

# arr = list(range(1,10))

# for i in arr:
#     print(f'{i:2.2f}')


# ## 튜플 for문 

# arr2 = ('me','my','friend','jane')

# for item in arr2:
#     print(f'{item:>200}')


# numbers = list(range(1,101,2 ))

# res = 0
# for i in numbers:
#     res += i

# print(f'{numbers[-1]} 까지의 총 합은 {res} 입니다')


## 홀수 짝수 구문

# numbers = list(range(1,21))

# for i in numbers:
#     if i % 2 == 1 : # 홀수
#         print(f'{i}은 홀수')


# 13이상이면 탈출 

# numbers = list(range(1,21))

# for i in numbers:
#     if i == 15 : # 홀수
#         continue

#     if i % 2 == 1 :
#         print(f'{i}는 홀수')
        

# for i in range(2,10):
#     for j in range(1,10):
#         print(f'{i} x {j} = {i*j} 입니다')


# print('구구단 프로그램')
# for x in range(2,10): # 2 ~ 9
#     print(f'{x}단 시작')
#     for y in range(1,10): # 1~ 9
#         print(f'{x} x {y} = {x*y:2d}', end='   ')
#     print()
    
print('구구단 프로그램')
for x in range(2,10): # 2 ~ 9
    if x == 8:
        continue
    for y in range(1,10): # 1~ 9
        print(f'{x} x {y} = {x*y:2d}', end='   ')
    print()
    
