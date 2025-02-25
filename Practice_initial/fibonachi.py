class Fibonachi:
    def calculate_nth(self, num:int):
        if num <=1:
            return num
        else:
            return self.calculate_nth(num-1) + self.calculate_nth(num-2)
