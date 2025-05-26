# Generic  classes for building reader functionalities 
# AUTHOR Sven Schrodt
# SINCE 2025-05-26

import json
import requests


class APIReader:
    """ Generic class for building HTTP API Clients

    Returns:
        _type_: _description_
    """
    to2f:str = '{}'
    scheme: str = 'https://'
    fqdn: str = 'foo.example.org'
    
    # ordered list of params
    ol_par:list = [43]
    
     # dict containing key-value pairs of|for params
    pars:list = {}
    
    endpoints: dict = {
        'root': '/',
        'look': '/lookp/id/{}',
        'inv': '/inv/'
    }

    def __init__(self):
        pass
    
    def gen_uri(self, ctx:str='root') -> str:
        if ctx not in self.endpoints:
            raise ValueError(f'the key {ctx} is not valid!')
        ep = self.endpoints[ctx]
        uri = f'{self.scheme}{self.fqdn}{ep}'
        if uri.find(self.to2f) != -1:
            uri = uri.format(*self.ol_par)
        return uri 
    
    def apd_pars(self) -> str:
        pass
        return ''

reader = APIReader()

ep1 = reader.gen_uri('look')
#ep1 =reader.gen_uri()
#print(ep1, ep1.find('{}'))

exit()
print(reader.gen_uri())
print(reader.gen_uri('inv'))