import http.client
import requests

#create a connection
conn = http.client.HTTPConnection("127.0.0.1",80)

def Send_get_resp():
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
    cmd = input("input command (ex. POST filename.txt): ")
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
go = True
while(go ==True):
    ans = input("[1] for GET [2] for POST ")
    if(ans == '1'):
        Send_get_resp()
    elif(ans == '2'):
        Send_post_resp()
    else:
        go = False
