class DataAnalyzer:
    def __init__(self):
        self.n = 0
        self.xsum = 0
        self.ysum = 0
        self.xysum = 0
        self.x2sum = 0
        self.y2sum = 0

    def add_point(self, x, y):
        self.n += 1
        self.xsum += x
        self.ysum += y
        self.xysum += x * y
        self.x2sum += x * x
        self.y2sum += y * y

    def calculate_error(self, a, b):
        return a * a * self.x2sum + self.y2sum - 2 * a * self.xysum + \
               2 * a * b * self.xsum - 2 * b * self.ysum + self.n * b * b