from pickle import TUPLE1


arr2 = [1,2,['HI','My','Friend']]
print(arr2[0])
print(arr2[2])
print(arr2[2][1])
print(arr2[2][1][0])

arr3 = list(range(1,4))
print(arr3)

print(arr3 * 3 )


print('-- 리스트 내장함수')
del(arr3[1])
print(arr3)

arr3.remove(1)
print(arr3)

arr4 = [12,4,2,6,9,12,16,7,1,3,3,5]
del(arr4[0])
print(arr4)

arr4.remove(12)
print(arr4)


arr5 = [1,2,3,4,5]
del(arr5[0])
print(arr5)
print(arr5[0])




dic1 = {1 :'a'}
dic1[2] = 'b'
print(dic1)

dic1['name'] = 'Hugo'
print(dic1)

del dic1['name']
print(dic1)

print(dic1.keys())
print(dic1.values())
print(dic1.items())



# 리스트 튜플 변환

print("---- 리스트 튜플 변환 ---- ")
print(arr4)
tup2 = tuple(arr4)
print(tup2)

arr4.sort()
arr5 = list(tup1)
