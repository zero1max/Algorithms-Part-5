class Calculate:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def qoshish(self):
        return self.a + self.b
    
    def ayirish(self):
        return self.a - self.b
    
    def kopaytirish(self):
        return self.a * self.b
    
    def bolish(self):
        return self.a / self.b
    
    def qoldiqsiz_bolish(self):
        return self.a // self.b
    
    def qoldiq_topish(self):
        return self.a % self.b


amal = Calculate(1, 2)
print(amal.qoshish())
print(amal.ayirish())
print(amal.kopaytirish())
print(amal.bolish())
print(amal.qoldiqsiz_bolish())
print(amal.qoldiq_topish())