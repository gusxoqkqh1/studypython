# Person.py
# Person 클래스


class Person:
    def __init__(self,name,age):
        self.name1 = name
        self.age1 = age
        print("Person이 생성되었습니다.")


    gender = ''
    feetsize = 250
    bloodtype = ''


## 객체의 행동 ( 메소드를 만든다 )  

    def 소개한다(self):
        gretting = f'''안녕하세요. 저는 {self.name} 입니다.
        {self.gender}구요. {self.age} 살입니다.
        '''
        print(gretting)

    def 먹는다(self, food):
        print(f'{self.name}이 {food}를 먹는다')
    
    def 일한다(self, drink):
        print(f'{self.name} 이 {self}를 마시면서 일한다')


# 사람 객체를 만들자

if __name__ == '__main__':

    htg = Person('홍태경',46)
    htg.소개한다()
    print(htg.age1)
    
    htg.소개한다()



    # htg.name = '홍태경'
    # htg.age = 31
    # htg.gender = '남자'
    # htg.feetsize = 
    # htg.bloodtype 'AB+'


    # htg.소개한다()
    # htg.먹는다('본죽')
    # htg.일한다('핫식스')
    # int


    # # p = Person() # p라는 이름의 Person 객체 생성
    # # print(type(p))
    # # print(id(p))


    # # p2 = Person()
    # # print(type(p2))
    # # print(id(p2))

    

