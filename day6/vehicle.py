

class Car:
    def __init__(self, 차량번호, 제조사, color, release):
        self.number  = 차량번호
        self.made    = 제조사
        self.color   = color
        self.release = release
    
    def __str__(self):
        return f'제 차는 {self.release}에 만들진 {self.made} 차량입니다.'


    def 전진한다(self):
        pass

    def 후진한다(self):
        pass

    def 좌회전한다(self):
        print(f'{self.number}가 좌회전 합니다')

    def 우회전한다(self):
        pass




if __name__ == '__main__':

    제네시스 = Car('123허.123','현대','레드',1992)
    print(제네시스.number)
    print(제네시스.made)
    print(제네시스.color)
    print(제네시스.release)

    
    print(제네시스.좌회전한다())

print(제네시스)