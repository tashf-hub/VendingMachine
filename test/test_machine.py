import unittest
from vendingmachine.vendingmachine import CSVReader,SellingBeverage

class TestCSVPrinter(unittest.TestCase):
    def setUp(self):
        self.printer = CSVReader("sample.csv")

    def test_allread(self):
        #すべての行を読んでいるか
        l = self.printer.read()
        self.assertEquals(2,len(l))
        print("test_allread")

    def test_split(self):
        #", "で区切られているか
        row0=self.printer.read()[0]
        self.assertEquals(2,len(row0))

    
    def test_not_exist_file(self):
        #存在しないファイルを読まないか
        with self.assertRaises(FileNotFoundError):
            printer = CSVReader("not_exist.csv")
            printer.read()

class TestSellingBeverage(unittest.TestCase):
    #get
    def test_get_name(self):
        drink=SellingBeverage("sample",100,2)
        self.assertEquals("sample",drink.get_name)
    
    def test_get_price(self):
        drink=SellingBeverage("sample",100,2)
        self.assertEquals(100,drink.get_price)

    def test_get_stock(self):
        drink=SellingBeverage("sample",100,2)
        self.assertEquals(2,drink.get_stock)
    
    #在庫がへるか
    def test_minusstock(self):
        drink=SellingBeverage("sample",100,2)
        drink.minus_stock()
        self.assertEquals(1,drink.stock)
        


