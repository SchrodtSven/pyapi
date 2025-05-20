import configparser

class Cfg:
    cfg_fn:str = "api.cfg.ini"
    config:configparser.ConfigParser = None
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.cfg_fn)
        
    def get_api_key(self, idx: str):
        return self.config["api_keys"][idx]

    

class APIList:
    #TODO get other cfg data from net.py
    api_list: dict

    def __init__(self):
        self.api_list = {
            "api_ninjas": {
                "uri": "https://api.api-ninjas.com/v1/{}?{}={}",
                "uri_tpl": ["ctx", "subject", "q"],
                "dta_root": "places",
                "description": "Several endpoints",
                "type": ["text/plain", "json"],
                "short_id": "zip",
                "cfg_idx": "api_ninjas", # used to get API key from (hidden, NOT committed) ini file)
                "header_key_name": "X-Api-Key"
            },
            "openweathermap": {
                "uri": "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}",
                "uri_tpl": ["lat", "lon", "API key"],
                "dta_root": "places",
                "description": "API with trivia on m3trix",
                "type": ["text/plain", "json"],
                "short_id": "zip",
                "cfg_idx": "openweathermap", # used to get API key from (hidden, NOT committed) ini file)
                "header_key_name": "appid"
            }
        }
    
    def get_dict(self, key:str):
        # FIXME: sanitize
        if 'api_key' not in self.api_list[key]:
            cfg = Cfg()
            self.api_list[key]['api_key'] = cfg.get_api_key(self.api_list[key]['cfg_idx'])
        return self.api_list[key]

    def get_headers(self, key:str):
        headers = {}
        headers[self.api_list[key]['header_key_name']] = self.api_list[key]['api_key']
        return headers  
    

class RESTList(APIList):
    
    foo:str
    bar:id
    
    def __init__(self):
        super().__init__()
        self.foo = 'shdjhs'
        self.bar = 42