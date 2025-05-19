# AUTHOR: Sven Schrodt<sven.schrodt@schrodt.club
# SINCE: 2025-05-19
import requests


class ApiReader:

    api_list: list
    lst_response: requests.models.Response
    dta: list

    def __init__(self):
        self.api_list = [
            {
                "uri": "http://numbersapi.com/{}/{}",
                "dta_root": "drinks",
                "description": "API with trivia on m3trix",
                "type": ['text/plain', 'json'],
            },
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
    
    def get(self, uri, dta_root='') -> list:
        self.lst_response = requests.get(uri)
        if dta_root == '':
            return self.lst_response.text
        else: 
            self.dta = self.lst_response.json()[dta_root]
    
        



