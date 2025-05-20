from net import ApiReader

#uri = 'http://localhost:8080/foo.php?id=Foo&name=Sven&Address=Schlumpfhausen'
payload_dict = {'first_name': 'Nev$23', 'profession': 'Mö$T 3v1l H@xXR'}
uri = 'http://localhost:8080/foo.php'
reader = ApiReader()
reader.put(
    uri = uri,
    data = payload_dict
)
print(reader.dta.text)
