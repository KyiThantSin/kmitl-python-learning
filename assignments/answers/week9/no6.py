class StationaryGood:
    def getCost(self):
        pass 

class Magazine(StationaryGood):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def getCost(self):
        return self.price * self.quantity

class Book(StationaryGood):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def getCost(self):
        discounted_price = self.price * 0.9
        return discounted_price * self.quantity

class Ribbon(StationaryGood):
    def __init__(self, color, length):
        self.color = color
        self.length = length  

    def getCost(self):
        return 5 * self.length

def getTotalCost(basket):
    total_cost = 0
    for item in basket:
        total_cost += item.getCost()  
    return total_cost

def main():
    magazine1 = Magazine("Computer World", 70, 3) 
    book1 = Book("Windows 7 for Beginners", 200, 2) 
    ribbon1 = Ribbon("Blue", 10) 
    
    basket = [magazine1, book1, ribbon1]
    total_cost = getTotalCost(basket)
    print(f"The total cost of the goods in the basket is {total_cost:.2f} Bahts")

if __name__ == "__main__":
    main()
