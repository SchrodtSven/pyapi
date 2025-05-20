import requests
import configparser

config = configparser.ConfigParser()



config.read('api.cfg.ini')
cfg = config.sections()

print(config['api_keys']['api_ninjas'])

exit(23)

word = 'Pestilence'
api_url = 'https://api.api-ninjas.com/v1/dictionary?word={}'.format(word)
response = requests.get(api_url, headers={'X-Api-Key': '+rc39OgeA4O8/lO3bWgKhQ==13Wl4bh3Eep2Y4d4'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)