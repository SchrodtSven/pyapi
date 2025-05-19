from net import ApiReader

reader = ApiReader()
# print(reader.api_list[0])


#exit(666)

uri = reader.api_list[0]['uri'].format('Mojito')
root = reader.api_list[0]['dta_root']
reader.get(uri, root)
resp = reader.lst_response

print(resp.text)