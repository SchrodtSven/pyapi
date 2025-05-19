from net import ApiReader
# Ascheberg et. al --> 59387

reader = ApiReader()
lang = "de"
zip =  '47445'
#zip = 59387
uri = reader.api_list[0]['uri'].format(lang, str(zip))
#print(uri)
#exit(88)
reader.get(
    uri = uri,
    dta_root='places'
)
#print(reader.lst_response.text)
print(reader.dta)

