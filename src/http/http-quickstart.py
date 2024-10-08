import http.client
import os

auth = 'Bearer '
try:
    auth += os.environ['EPHONE_AI_KEY']
except KeyError:
    print("No API key provided")

payload = ''
conn = http.client.HTTPSConnection("api.ephone.chat")
headers = {
    'Authorization': auth,
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
}
conn.request("GET", "/v1/models", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
