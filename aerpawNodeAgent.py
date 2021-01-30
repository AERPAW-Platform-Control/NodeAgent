import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Sending an '200 OK' response
        self.send_response(200)

        # Setting the header
        self.send_header("Content-type", "text/plain")

        # Whenever using 'send_header', you also have to call 'end_headers'
        self.end_headers()

        pathStr = self.path
        pathLen = len(pathStr)


        if pathStr.startswith("/v1/fetchContainer/") :
            # service fetchContainer
            returnedStr = "OK"
            print("Doing a fetchContainer")
        elif pathStr.startswith("/v1/startContainer") :
            # service startContainer
            returnedStr = "OK"
            print ("Doing a startContainer")
        else :
            returnedStr = "UNKNOWN"


        # Writing the resulting contents with UTF-8
        self.wfile.write(bytes(returnedStr, "utf8")) # FIXME - probably shouldn't be UTF-8?

        return

# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 1887
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()

