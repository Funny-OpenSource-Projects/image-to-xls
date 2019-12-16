import re
import openpyxl, os
from openpyxl.styles import PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.styles import Color, Fill
from http.server import BaseHTTPRequestHandler 
from PIL import Image 

class handler(BaseHTTPRequestHandler):

    def do_POST(self):

        content_length = int(self.headers['Content-Length']) 
        post_data = self.rfile.read(content_length) 

        self.send_response(200)
        #self.send_header("Accept-Ranges", "bytes")
        self.send_header("Access-Control-Allow-Origin", "*")
        #self.send_header("Content-Disposition", "attachment")
        #self.send_header("Content-Length", len(message))
        #self.send_header("Content-type", "image/svg+xml")
        self.end_headers()
        self.wfile.write(str(post_data).encode())
        return  