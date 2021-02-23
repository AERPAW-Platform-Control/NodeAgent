#!/usr/bin/env python3

import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs
import subprocess
import os

def runCmd(cmd):
    #shelledResults = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    shelledResults = subprocess.run(cmd, shell=True)
    #print ("stdout = " + shelledResults.stdout)
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

        respond=True
        if self.path.startswith("/v1/fetchContainer/") :
            returned=bytes("OK","utf-8")
            respond=True
            print("Doing a fetchContainer of " + containerStr)
            command = "./fetchContainer " + containerStr
            runCmd(command)

        elif self.path.startswith("/v1/fetchVM/") :
            returned=bytes("OK","utf-8")
            print ("Doing a fetchVM of " + containerStr )
            command = "fetchVM " + containerStr
            runCmd(command)
            
        elif self.path.startswith("/v1/startContainer/") :
            returned=bytes("OK","utf-8")
            respond=True
            print ("Doing a startContainer of " + containerStr )
            command = "startContainer " + containerStr
            runCmd(command)

        elif self.path.startswith("/v1/startVM/") :
            returned=bytes("OK","utf-8")
            print ("Doing a startVM of " + containerStr )
            command = "startVM " + containerStr
            runCmd(command)            

        elif self.path.startswith("/v1/emitDataVolume/") :
            print ("Doing an emitDataVolume of " + containerStr )
            # 1: tar the directory
            # 2: loop, reading a megabyte, writing a MB.
            respond=False  # we're doing the response in here, no need to at the bottom.
            tarCommand = "tar cf /var/local/outputs/" + containerStr + ".tar /var/local/outputs/" + containerStr + " /var/local/outputs/" + containerStr + "-stdout /var/local/outputs/" + containerStr + "-stderr"
            runCmd(tarCommand)
            # OK, TODO: This is just a quick hack to show tomorrow, need to
            # make this loop and not allocate 20+G of RAM, potentially.
            with open("/var/local/outputs/" + containerStr + ".tar", 'rb') as file:
                tarFileContents=file.read(-1)
            self.wfile.write(tarFileContents)

        elif self.path.startswith("/v1/deleteDataVolume/") :
            returned=bytes("OK","utf-8")
            respond=True
            print ("Doing a deleteDataVolume of " + containerStr )
            tarCommand = "rm -rf /var/local/outputs/" + containerStr + " /var/local/outputs/" + containerStr + "-stdout /var/local/outputs/" + containerStr + "-stderr"
            runCmd(rmCommand)


        elif self.path.startswith("/v1/killContainer/") :
            returned=bytes("OK","utf-8")
            respond=True
            print ("Doing a killContainer of " + containerStr )
            killCmd="docker kill " + containerStr
            runCmd(killCmd)
            
        else :
            returned=bytes("Unknown REST entrypoint","utf-8")
            respond=True


            # Writing the resulting contents with UTF-8
        if respond == True:
            self.wfile.write(returned)

        return


class MyServer(socketserver.TCPServer):
    allow_reuse_address=True

    
# Create an object of the above class
handler_object = MyHttpRequestHandler

runCmd("ls")
PORT = 1887
#my_server = socketserver.TCPServer(("", PORT), handler_object)
my_server = MyServer(("",PORT), handler_object)

# Star the server
my_server.serve_forever()

