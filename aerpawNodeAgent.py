import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs
import subprocess

def runCmd(cmd):
    shelledResults = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return shelledResults.returncode

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Sending an '200 OK' response
        self.send_response(200)

        # Setting the header
        self.send_header("Content-type", "text/plain")

        # Whenever using 'send_header', you also have to call 'end_headers'
        self.end_headers()

        print("Handling: " + self.path)
        pathPiecesList = self.path.split("/")
        containerStr = pathPiecesList[3]
        print("zeroeth element =" + pathPiecesList[0])


        if self.path.startswith("/v1/fetchContainer/") :
            # service fetchContainer
            returnedStr = "OK"
            print("Doing a fetchContainer of " + containerStr)
            command = "fetchContainer " + containerStr
            runCmd(command)

        elif self.path.startswith("/v1/startContainer/") :
            # service startContainerWithMount
            returnedStr = "OK"
            print ("Doing a startContainer of " + containerStr )
            command = "startContainer " + containerStr
            runCmd(command)

        elif self.path.startswith("/v1/emitDataVolume/") :
            # service startContainerWithMount
            returnedStr = "OK"
            print ("Doing an emitDataVolume of " + containerStr )

        elif self.path.startswith("/v1/deleteDataVolume/") :
            # service startContainerWithMount
            returnedStr = "OK"
            print ("Doing a deleteDataVolume of " + containerStr )

        elif self.path.startswith("/v1/killContainer/") :
            # service startContainerWithMount
            returnedStr = "OK"
            print ("Doing a killContainer of " + containerStr )
            
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

