from http.server import BaseHTTPRequestHandler,HTTPServer
import os

class ClientHandler(BaseHTTPRequestHandler):
    #user_name = input("Please enter your username: ")#your computer name

    #handle a GET request
    def do_GET(self):
        #file location
        rootdir = 'C:/Users/marquies/Desktop/'
        try:
            if self.path.endswith('.txt'):
                f = open(rootdir + self.path)#opens the requested file
                print(f.readline())
                #packing the header files together
                self.send_response(200,0)#ok
                #specify the type you are handling
                self.send_header("Content-type", "text/txt")
                self.end_headers()

                #send the file contents to client
                self.wfile.write(bytes(f.readline(),"utf-8"))
                f.close()
                return
        except IOError:
            self.send_error(404,'it is not your turn yet')

    #Handle a POST request
    def do_POST(self):
        rootdir = 'C:/Users/marquies/Desktop/'
        try:
            content_length = int(self.headers['Content-Length'])
            file_content = self.rfile.read(content_length)
            print(file_content)

            if self.path.endswith('.txt'):
                f = open(rootdir + self.path,"w")#opens the requested file
                f.write(str(file_content))

            #packing the header files together
            self.send_response(200,1)#ok
            self.end_headers()
        except IOError:
            self.send_error(404,'file not found')

#-------------------------THE SERVER------------------------

#this is how you create and run the server
def run(server_class = HTTPServer, handler_class = ClientHandler):
    print("http server is starting...")
    server_address = ('140.182.22.241',6000)#connect to this location
    httpd = server_class(server_address,handler_class)
    print("http is running...")
    httpd.serve_forever()

if(__name__ == '__main__'):
   run()
