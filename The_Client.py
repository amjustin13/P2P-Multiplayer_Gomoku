import http.client

#create a connection
conn = http.client.HTTPConnection("localhost",80)

def Send_get_resp():
    #create a connection
    conn = http.client.HTTPConnection("localhost",80)

    cmd = input("input command (ex. GET index.txt): ")
    cmd = cmd.split()

    if cmd[0] == 'exit':
        exit(0)
    #request command to server
    conn.request(cmd[0],cmd[1])

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
    #cmd = input("input command (ex. POST filename.txt): ")
    #cmd = cmd.split()

    #if cmd[0] == 'exit':
    #    exit(0)

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

# go = True
#
# while(go ==True):
#    ANS = input("[1] FOR GET [2] FOR POST ")
#    if(ANS == '1'):
#        Send_get_resp()
#    elif(ANS == '2'):
#        Send_post_resp_RESP()
#    else:
#     #    go = False
