import requests


class ApiReader:

    api_list: list
    lst_response: requests.models.Response
    dta: list

    def __init__(self):
        self.api_list = [
            {
                "uri": "https://www.thecocktaildb.com/api/json/v1/1/search.php?s={}",
                "dta_root": "drinks",
                "description": "Cocktail Recipes",
                "type": "json",
            },
            {
                "uri": "https://opentdb.com/api.php?amount={}",
                "dta_root": "results",
                "description": "open trivia database",
                "type": "json",
            },
        ]
    
    def get(self, uri, dta_root) -> list:
        self.lst_response = requests.get(uri)
        self.dta = self.lst_response.json()[dta_root]
        



