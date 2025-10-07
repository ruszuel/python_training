from utils.file_util import read_json_as_dict

class BaseRates:
    def retrieve_rates(self):
        return read_json_as_dict("rates.json")
