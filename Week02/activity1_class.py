class TestMath:
    def __init__(self, n):
        self.num = n
        self.kept_num = n

    def reset(self):
        self.num = self.kept_num
    
    def get_factorial(self):
        if self.num > 1:
            self.num = self.num - 1
            return self.num * self.get_factorial()    
    
        return 1
    
    def get_fibonacci(self, lst_resulted = None):
        if lst_resulted is None:
            self.reset()
            lst_resulted = self.num * [0]
        else:
            self.num = self.num - 1
            
        if self.num <= 0:
            return lst_resulted
        elif self.num == 1:
            lst_resulted[0] = 0
            return lst_resulted
        elif self.num == 2:
            lst_resulted[0], lst_resulted[1] = 0, 1
            return lst_resulted 
        else:
            if lst_resulted[self.num-1] == 0:
                self.get_fibonacci(lst_resulted)
                lst_resulted[self.num-1] = lst_resulted[self.num-2] + lst_resulted[self.num-3]
            return lst_resulted 


num = int(input("Give a number:"))
test_math = TestMath(num)
print(f"Factorial: {test_math.get_factorial()}")
print(f"Fibonacci: {test_math.get_fibonacci()}")