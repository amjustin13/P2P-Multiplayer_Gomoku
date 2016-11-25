import http.client

conn = http.client.HTTPConnection("74.215.83.229")
conn.request("GET", "/boxes.py")
r1 = conn.getresponse
print(r1.status, r1.reason)

data1 = r1.read()
print(data1)
conn.close()
