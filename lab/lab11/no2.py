class Calculator(object):
    def __init__(self, acc = 0):
        self.acc = float(acc)
    
    def set_accumulator(self,a):
        self.acc = float(a)

    def get_accumulator(self):
        return self.acc
    
    def add(self,x):
        self.acc = self.acc + float(x)
    
    def subtract(self, x):
        self.acc = self.acc - float(x)
    
    def multiple(self, x):
        self.acc = self.acc * float(x)
    
    def divide(self, x):
        self.acc = self.acc / float(x)
    
    def print_result(self):
        print("Result:", self.acc)

class Sci_calc(Calculator):
    def __init__(self, acc):
        super().__init__(acc)
        
    def square(self):
        self.acc = self.acc * self.acc
    
    def exp(self, x):
        self.acc = self.acc ** x

    def factorial_iterative(self,n): 
        result = 1
        for i in range(1, n+1):
            result *= i
        return result
    
    def factorial(self,n):
        if n == 0 or n == 1:
            return 1
        else:
            self.acc = n * self.factorial_iterative(n-1)
    
    def print_result(self):
        print("Result", format(self.acc, "10.2e"))

number = Sci_calc(34)
number.subtract(4)
number.print_result()