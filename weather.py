from cfg import APIList, Cfg
from net import ApiReader

api_to_use = 'openweathermap'
apis = APIList()
ninja = apis.get_dict(api_to_use)



uri = ninja['uri'].format('51.4321', '6.7644',  '45599a0137d4a8fdd265d79afe63cab3')
print(uri)

#headers = apis.get_headers(api_to_use)
#headers['X-Api-Key'] = '*************************'
#print(ninja)
#print(headers)



