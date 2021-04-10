import http.server
import socketserver
from http import HTTPStatus
import random
import time

SERVER_START_TIME  = time.time()
def get_quotes():
    QUOTES = []
    with open('quotes.txt') as quotes_f:
        quote = ''
        for line in quotes_f:
            if not line.strip():
#                print('EMPTY LINE')
                continue
            quote += line
            if line[0]  == '-' :
#                print('New line.....')
#                print('QUOTE', quote)
                QUOTES.append(quote)
                quote = ''
    if quote:
        QUOTES.append(quote)
    return QUOTES


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(bytearray(QUOTES[random.randrange(len(QUOTES))], 'utf-8'))
        self.wfile.write(bytearray('\n\t\t\t\t\tTimestamp:{}'.format(SERVER_START_TIME), 'utf-8'))

print('Reading Quotes from file')
QUOTES = get_quotes()

httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()
