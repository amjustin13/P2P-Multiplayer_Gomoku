import http.client
def Send_get_resp():
   #request command to server
   conn.request('GET','game state.txt')

   #get response from server
   response = conn.getresponse()

   #print server response and data
   print("printing response...")
   print(int(response.status), response.reason)
   data_recieved = response.read()
   print(data_recieved)
   conn.close()

def Send_post_resp():
    #create a connection
    conn = http.client.HTTPConnection("localhost",80)#192.168.0.24:6000

    #request command to server
    conn.request('POST','game state.txt')
    #get response from server
    response = conn.getresponse()

    #print server response and data
    print("printing response...")
    print(int(response.status), response.reason)
    data_recieved = response.read()
    print(data_recieved)
    conn.close()
