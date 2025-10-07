from bll.rates_bll import RatesBll

class Rates:
    def __init__(self):
        self.rates = RatesBll()

    def display_conversion(self, source, target, amount) -> float:
       return self.rates.convert_money(source, target, amount)