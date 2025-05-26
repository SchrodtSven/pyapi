from cfg import APIList, Cfg
from net import ApiReader

api_to_use = 'openweathermap'
apis = APIList()
ninja = apis.get_dict(api_to_use)
