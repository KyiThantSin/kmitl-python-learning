class Poly:
    def __init__(self, x):
        self.x = x

    def add(self, p):
        result = []
        max_len = max(len(self.x), len(p.x))
        for i in range(max_len):
            c1 = self.x[i] if i < len(self.x) else 0
            c2 = p.x[i] if i < len(p.x) else 0
            result.append(c1 + c2)
        return Poly(tuple(result))

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
    
    def power(self, n):
        result = Poly((1,))
        for _ in range(n):
            result = result.multiply(self)
        return result

    def diff(self):
        if len(self.x) <= 1:
            return Poly((0,))
        result = [i * self.x[i] for i in range(1, len(self.x))]
        return Poly(tuple(result))

    def integrate(self):
        result = [0] + [self.x[i] / (i + 1) for i in range(len(self.x))]
        return Poly(tuple(result))

    def eval(self, n):
        result = 0
        for i in range(len(self.x)):
            result += self.x[i] * (n ** i)
        return result

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

q = p.power(2)
q.print() 
print(p.eval(3)) 
     
r = p.add(Poly((1, -2, 0)))
r.print() 

s = r.diff()
s.print() 

p2 = p.scalar_multiply(2)
p2.print()

p3 = p.add(p2)
p3.print()

r = p.multiply(p)
r.print()