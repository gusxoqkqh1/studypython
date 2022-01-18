#변수 라이프스코프

from re import A


a = 1              ## 로컬 변수
res = 0 
def vartest(x):    ## 지역 변수
    x = x + 1
    return x

res = vartest(a)     ## a = 로컬 변수 
print(a)
print(res)