from http.server import BaseHTTPRequestHandler,HTTPServer
import os
global player
player = 0

class ClientHandler(BaseHTTPRequestHandler):
    user_name = input("Please enter your username: ")#your computer name
    #handle a GET request
    def do_GET(self):
        global player
        player = 1
        #file location
        rootdir = 'C:/Users/'+self.user_name+'/Desktop/'
        try:
            if self.path.endswith('.txt'):
                f = open(rootdir + self.path)#opens the requested file

                #packing the header files together
                self.send_response(200)#ok
                #specify the type you are handling
                self.send_header("Content-type", "text/txt")
                self.end_headers()

                #send the file contents to client
                self.wfile.write(bytes(f.readline(),"utf-8"))
                f.close()
                return
        except IOError:
            self.send_error(404,'file not found')

    #Handle a POST request
    def do_POST(self):
        global player
        player = 0#enables player to make a move
        try:
                #packing the header files together
                self.send_response(200)#ok
                self.end_headers()
                return
        except IOError:
            self.send_error(404,'file not found')

#-------------------------THE SERVER------------------------

#this is how you create and run the server
def run(server_class = HTTPServer, handler_class = ClientHandler):
    print("http server is starting...")
    server_address = ('149.162.139.182',80)#connect to this location
    httpd = server_class(server_address,handler_class)
    print("http is running...")
    httpd.serve_forever()

if(__name__ == '__main__'):
   run()
