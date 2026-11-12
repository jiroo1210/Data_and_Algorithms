class DataAnalyzer:
    def __init__(self):
        # TODO keep track of sum((y_i-(ax_i+b))^2) sq. error for y= ax +b
        # expand y**2 -2y(ax+b) +(ax +b)**2
        # y**2 -2axy -2by + a**2x**2 + 2abx + b^2
        # keep track of 1. sum(y**2); 2. -2a*sum(x*y); 3. -2b*sum(y)
        # 4. a**2 * sum(x**2); 5. 2ab*sum(x) 6. b^2 *n 
        self.list = []
        self.dict = {i:0 for i in range(1,7)}

    def add_point(self, x, y):
        # TODO add an observation to the data
        self.list.append((x,y))
        self.dict[1] += y**2 # 1
        self.dict[2] += x*y # -2a
        self.dict[3] += y # -2b
        self.dict[4] += x**2 # a**2
        self.dict[5] += x # 2ab
        self.dict[6] += 1 # b^2
                

    def calculate_error(self, a, b):
        # TODO return the sum of squares error for the given line parameters
        total = 0
        total += self.dict[1] - self.dict[2]*(2*a) - self.dict[3]*(2*b)
        total += self.dict[4]*(a**2) + self.dict[5]*2*a*b + self.dict[6]*(b**2)

        return total

if __name__ == "__main__":
    analyzer = DataAnalyzer()

    analyzer.add_point(1, 1)
    analyzer.add_point(3, 2)
    analyzer.add_point(5, 3)
    print(analyzer.calculate_error(1, 0)) # 5
    print(analyzer.calculate_error(1, -1)) # 2
    print(analyzer.calculate_error(3, 2)) # 293

    analyzer.add_point(4, 2)
    print(analyzer.calculate_error(1, 0)) # 9
    print(analyzer.calculate_error(1, -1)) # 3
    print(analyzer.calculate_error(3, 2)) # 437

    analyzer = DataAnalyzer()
    total = 0
    for i in range(10**5):
        analyzer.add_point(i, i % 100)
        total += analyzer.calculate_error(i % 97, i % 101)
    print(total) # 25745448974503313754828