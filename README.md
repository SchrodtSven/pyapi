# PyApi
API client (HTTP based) 



## Basic usage

### Pseudo example
```python

reader = ApiReader()
reader.get('https://example.net/v1/user/12345', 'root_ele')
resp = reader.lst_response
```


### Working example
```python
from net import ApiReader
uri = reader.api_list[0]['uri'].format('Mojito')
root = reader.api_list[0]['dta_root']
reader.get(uri, root)
resp = reader.lst_response
```


## Appendix 

### API rel. external resources

- https://rapidapi.com/collection/list-of-free-apis