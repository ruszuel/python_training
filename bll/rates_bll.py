from dal.rates_dal import BaseRates

class RatesBll:
    def __init__(self):
        self.data = BaseRates().retrieve_rates()
        
    def convert_money(self, source: str, target: str, amount: float):
        base = self.data["base"]
        rates = self.data["rates"]

        if source == target:
            return f"{amount} {source} = {amount} {target}"

        try:
            if source == base and target in rates:
                rate = rates[target]
                converted = amount * rate
                return f"{amount} {source} = {converted:.2f} {target}"
            elif target == base and source in rates:
                rate = rates[source]
                converted = amount / rate
                return f"{amount} {source} = {converted:.2f} {target}"
            elif source in rates and target in rates:
                to_php = rates[source]
                converted_php =  amount / to_php
                target_curr = rates[target]
                converted_value = converted_php * target_curr
                return f"{amount} {source} = {converted_value:.2f} {target}"
            else:
                return "Conversion not supported with current rates.json structure."
        except Exception:
            return 'Error occured'


