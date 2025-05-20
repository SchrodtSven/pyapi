from net import ApiReader


payload_dict = {'first_name': 'Peter', 'loc': 'Neverland'}
uri = 'http://localhost:8080/foo.php'
reader = ApiReader()
reader.put(
    uri = uri,
    data = payload_dict
)
print(reader.dta.text)
