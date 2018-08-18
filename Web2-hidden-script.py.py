import requests
from bs4 import BeautifulSoup

data = { 
    'c': '17331',
    's': '3a63031abfd017371a9a0fa615b977ef4a46613d87f6a104584142e44a4f75ec'
}
while True:
    r = requests.post('http://104.199.235.135:31332/_hidden_flag_.php', data=data)
    soup = BeautifulSoup(r.text, "html5lib")
    data['s'] = soup.select("input[name='s']")[0]['value']
    data['c'] = soup.select("input[name='c']")[0]['value']
    print(data['c'], data['s'])
    if "Hmm ... no flag here!" not in r.text:
        print(r.headers['Flag'])
        break