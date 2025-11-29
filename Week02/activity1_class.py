class TestMath:
    def __init__(self, n):
        self.num = n
        self.kept_num = n
    
    def get_factorial(self):
        if self.num > 1:
            self.num = self.num - 1
            return self.num * self.get_factorial()    
    
        return 1
    
    def fibonacci(self, n, lst_resulted = None):
        #Preparing a blank array at first
        if lst_resulted is None:
            lst_resulted = n * [0]
        
        if n <= 0:
            return lst_resulted
        elif n == 1:
            lst_resulted[0] = 0
            return lst_resulted
        elif n == 2:
            lst_resulted[0], lst_resulted[1] = 0, 1
            return lst_resulted 
        else:
            if lst_resulted[n-1] == 0:
                self.fibonacci(n-1, lst_resulted)
                lst_resulted[n-1] = lst_resulted[n-2] + lst_resulted[n-3]
            return lst_resulted  
    
    def get_fibonacci(self):
        return self.fibonacci(self.kept_num, None)


num = int(input("Give a number:"))
test_math = TestMath(num)
print(f"Factorial: {test_math.get_factorial()}")
print(f"Fibonacci: {test_math.get_fibonacci()}")