class MathDojo:
    def __init__(self):
        self.result = 0

    # Add numbers
    def add(self, num, *nums):
        self.result += num

        for number in nums:
            self.result += number

        return self

    # Subtract numbers
    def subtract(self, num, *nums):
        self.result -= num

        for number in nums:
            self.result -= number

        return self


# Create object
md = MathDojo()

# Method chaining
x = md.add(2).add(2, 5, 1).subtract(3, 2).result

print(x)   # 5


# More tests
md2 = MathDojo()

md2.add(10, 5).subtract(3).add(1, 1, 1).subtract(2, 2)

print(md2.result)