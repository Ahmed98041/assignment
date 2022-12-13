class StockItem:
    category = "Car accessories"

    def __init__(self, stock_code: str, quantity: int, price: float):
        self.stock_code = stock_code
        self.quantity = quantity
        self.price = price
        self.stock_name = "Unknown Stock Name"
        self.stock_description = "Unknown Stock Description"

    def setStockName(self, stock_name: str):
        self.stock_name = stock_name

    def setStockDescription(self, stock_description: str):
        self.stock_description = stock_description

    def getStockName(self):
        return self.stock_name

    def getStockDescription(self):
        return self.stock_description

    def increaseStock(self, amount: int):
        if amount < 1:
            print("Error: Invalid stock increase amount")
            return False
        else:
            self.quantity += amount
            return True

    def sellStock(self, amount: int):
        if amount < 1:
            print("Error: Invalid stock sell amount")
            return False
        elif amount <= self.quantity:
            self.quantity -= amount
            return True
        else:
            return False

    def getVAT(self):
        return 17.5
    def getPriceWithVAT(self):
        vat = self.getVAT()
        return self.price * (1 + vat / 100)

    def getPriceWithoutVAT(self):
        return self.price

    def __str__(self):
       stock_code = self.stock_code
       stock_name = self.getStockName()
       stock_description = self.getStockDescription()
       quantity = self.quantity
       price_before_vat = self.getPriceWithoutVAT()
       price_after_vat = self.getPriceWithVAT()
       return (
        f"Stock Code: {stock_code}\n"
        f"Stock Name: {stock_name}\n"
        f"Description: {stock_description}\n"
        f"Quantity in Stock: {quantity}\n"
        f"Price before VAT: {price_before_vat}\n"
        f"Price after VAT: {price_after_vat}"
    )

class NavSys(StockItem):
    def __init__(self, brand: str, stock_code: str, quantity: int, price: float):
        super().__init__(stock_code, quantity, price)
        self.brand = brand 

    def getStockName(self):
        return "Navigation system"

    def getStockDescription(self):
        return "GeoVision Sat Nav"

    def __str__(self):
        return super().__str__() + f"\nBrand: {self.brand}"

nav_sys = NavSys("GeoVision", "987", 500, 99.99)
print(nav_sys)


