class Money:
    def __init__(self, whole, kopecks, currency):
        self.whole = whole
        self.kopecks = kopecks
        self.currency = currency

    def infoMoney(self):
        print(f"{self.currency} - {self.whole}.{self.kopecks}")


class Result(Money):
    def __init__(self, whole, kopecks, currency):
        super().__init__(whole, kopecks, currency)
        self.whole = whole
        self.kopecks = kopecks
        self.currency = currency


obj = Result(100, 25, 'RU')
obj.infoMoney()
