class Poly:
    def __init__(self, x):
        self.x = x

    def add(self,p):
        print(self.x[0])
    
    def scalar_multiply(self, n):
        result = [value * n for value in self.x]
        return Poly(tuple(result))

    def multiply(self, p):
        result = []
        for i in range(len(self.x)):
            for j in range(len(p.x)):
                if i + j >= len(result):
                    result.append(0)
                result[i + j] += self.x[i] * p.x[j]

        return Poly(tuple(result))

    def print(self):
        result = ""
        for i in range(len(self.x)):
            value = self.x[i]
            if value == 0:
                continue

            if value > 0 and result != "":
                result += " + "
            elif value < 0 and result != "":
                result += " - "
            elif value < 0 and result == "":
                result += "-"

            abs_value = abs(value)
            if i == 0:
                result += f"{abs_value}"
            elif i == 1:
                if abs_value == 1:
                    result += "x"
                else:
                    result += f"{abs_value}x"
            else:
                if abs_value == 1:
                    result += f"x^{i}"
                else:
                    result += f"{abs_value}x^{i}"

        print(result)


p = Poly((1, 0, -2))
p.print()

p2 = p.scalar_multiply(2)
p2.print()

r = p.multiply(p)
r.print()