# # 함수 선언 및 사용


# # 더하기 함수 선언 
# def add(a,b):
#     res = a + b
#     return res

# # 함수 사용 
# hello = add(2464,879)
# print(f'총 합은 : {hello * 3} 입니다.')


# def say_hello():
#     return 'hello'

# print(say_hello())
# print(say_hello(),'my friend~')

# val = say_hello()
# print(val.replace('~',''))



# def say_hello(name):
#     print(f'Hello~{name}')

# say_hello('Hugo')


# def say_goodbye():
#     print('Bye bye~')

# say_goodbye()


# from audioop import mul


# def multi(a,b):
#     return a * b

# print(multi(2,9))
# print(multi(8,9))


## 매개변수 개수가 가변적일때

# def plus(*args):
#     res = 0 
#     for i in (args):
#         res += i
    
#     return res


# print(plus(1,2,3))
# print(plus(1,2,3,4,5,6,7))
# print(plus())



# ## 함수 결과가 하나 이상인 경우 
# def mul_and_div(x,y):
#     mul = x * y
#     div = x / y
#     return mul, div

# (res1, res2) = mul_and_div(10,5)
# print(res1)
# print(res2)



def 사칙연산(x,y):
    return (x+y,x-y,x*y)

res1, res2, res3 = 사칙연산(9,8)
print(res1,res2,res3)
print(type(사칙연산(1,2)))