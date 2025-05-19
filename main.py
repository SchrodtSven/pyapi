# AUTHOR: Sven Schrodt<sven.schrodt@schrodt.club
# SINCE: 2025-05-19
from net import ApiReader

reader = ApiReader()
# print(reader.api_list[0])


#exit(666)

uri = reader.api_list[0]['uri'].format(666, 'math?json')
#root = reader.api_list[0]['dta_root']
#print(uri)

#exit(355)

reader.get(uri)
resp = reader.lst_response

print(resp.json())