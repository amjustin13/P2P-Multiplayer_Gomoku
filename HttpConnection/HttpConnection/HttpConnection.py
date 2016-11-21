import http.client
import urllib.parse
import pygame 

#------------------This is how you GET a request--------
connect = http.client.HTTPConnection('www.google.com')
connect.request("GET","/")
responce = connect.getresponse()

#print(responce.status,responce.reason)

#this will return the entire content
data1 = responce.read()
#_____________________________________________________________
print("heelo")



      