# AUTHOR: Sven Schrodt<sven.schrodt@schrodt.club
# SINCE: 2025-05-19
import requests


class ApiReader:

    api_list: list
    lst_response: requests.models.Response

    def __init__(self):
        self.api_list = [
            {
                "uri": "https://api.zippopotam.us/{}/{}",
                "uri_tpl": ["lang", "number"],
                "dta_root": "places",
                "description": "API with trivia on m3trix",
                "type": ["text/plain", "json"],
                "short_id": "zip",
            },
            {
                "uri": "http://numbersapi.com/{}/{}",
                "uri_tpl": ["number", "type"],
                "description": "API with trivia on m3trix",
                "type": ["text/plain", "json"],
                "short_id": "numbers",
            },
            {
                "uri": "https://www.thecocktaildb.com/api/json/v1/1/search.php?s={}",
                "uri_tpl": ["q"],
                "dta_root": "drinks",
                "description": "Cocktail Recipes",
                "type": "json",
                "short_id": "drinks",
            },
            {
                "uri": "https://opentdb.com/api.php?amount={}",
                "uri_tpl": ["amount"],
                "dta_root": "results",
                "description": "open trivia database",
                "type": "json",
                "short_id": "trivia",
            },
        ]

    def get(self, uri, dta_root="", headers=[]):
        self.lst_response = requests.get(uri, headers=headers)
        if dta_root == "":
            self.dta = self.lst_response.text
        else:
            self.dta = self.lst_response.json()[dta_root]

    def post(self, uri, dta_root="", headers=[], payload_dict={}, data=""):
        self.lst_response = requests.post(
            uri, headers=headers, json=payload_dict, data=data
        )
        if dta_root == "":
            self.dta = self.lst_response
        else:
            self.dta = self.lst_response.json()[dta_root]

    def put(self, uri, dta_root="", headers=[], payload_dict={}, data=""):
        self.lst_response = requests.put(
            uri, headers=headers, json=payload_dict, data=data
        )
        if dta_root == "":
            self.dta = self.lst_response
        else:
            self.dta = self.lst_response.json()[dta_root]
