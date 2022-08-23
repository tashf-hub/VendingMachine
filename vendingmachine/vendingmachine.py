import csv
from webbrowser import get

class CSVReader:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        #csvを配列
        with open(self.file_name) as f:
            reader = csv.reader(f)
            lines = [row for row in reader]
        return lines
    

class SellingBeverage:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def get_stock(self):
        return self.stock
    def minus_stock(self):
        self.stock=self.stock-1


class VendingMachine:
    def __init__(self,filename):#"selling.csv"
        reader=CSVReader(filename)
        beverages=reader.read()
        self.beverages=[]
        for beverage in beverages:
            drink=SellingBeverage(beverage[0],int(beverage[1]),int(beverage[2]))
            self.beverages.append(drink)
    def sell(self,money,bevarage_name):
        drink=self.get_drink_by_name(bevarage_name)
        if drink == None:
            return None
        if(self.is_enough_money(money,bevarage_name)):
            if(self.exist_stock(bevarage_name)):
                drink.minus_stock()
                print(drink.get_name(),)
                return drink
        return None
    def get_drink_by_name(self,name):
        index=None
        for beverage in self.beverages:
            if beverage.get_name()==name:
                index=beverage
        return index
    def is_enough_money(self,money,bevarage_name) -> bool:
        drink=self.get_drink_by_name(bevarage_name)
        return money>=drink.get_price()
    def exist_stock(self,bevarage_name) -> bool:
        drink=drink=self.get_drink_by_name(bevarage_name)
        return 0<drink.get_stock()
    
"""
if __name__=="__main__":
    machine=VendingMachine("selling.csv")
    machine.sell(200,"cola")
    """