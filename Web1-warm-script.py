import requests

print(''.join([requests.get("http://104.199.235.135:31331/index.php?p={index}".format(index=i)).headers['Partial-Flag'] if requests.get("http://104.199.235.135:31331/index.php?p={index}".format(index=i)).headers['Partial-Flag'] != '' else ' ' for i in range(100)]))