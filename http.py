import SimpleHTTPServer
import SocketServer
import BaseHTTPServer
import os
import optparse

parser = optparse.OptionParser()
parser.add_option("-p", "--port", dest="PORT", type="int", help="Define port for server to use.")
parser.add_option("-r", "--root", dest ="ROOT", type="string", help="Set server root document.")
(options, args) = parser.parse_args()

HOSTNAME = "localhost"

# PORT = 8000
options.PORT = 8000
options.ROOT = '/home/mantavya294/projects/HTTPServer/httpserverDirectory'
HANDLER = SimpleHTTPServer.SimpleHTTPRequestHandler

os.chdir(options.ROOT)

httpd = SocketServer.TCPServer((HOSTNAME, options.PORT), HANDLER)

print "Server running on port ", options.PORT
httpd.serve_forever()
